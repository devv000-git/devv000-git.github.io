# Windows Memory Forensics and Process Hollowing Investigation

**Source:** SIT324 Malware Analysis, Deakin University, 2026  
**Exercises:** Task 8.3D (corrected memory-forensic report) and Task 9.1P (guest-based acquisition and hollowing investigation)  
**Source PDF pages:** **211–219** and **222–226**  
**Environment:** Isolated Windows virtual machines, Volatility 3, VirtualBox, FTK Imager, ProcWatch, Process Explorer

## Executive summary

Investigated suspicious execution inside Windows processes in **two distinct university laboratory exercises**. The first examined `ngentask.exe` (PID 5932) in a VirtualBox memory image for loader-list anomalies and private executable memory. The second correlated ProcWatch, Process Explorer and Volatility findings to investigate a suspicious `svchost.exe` (PID 3176) created by the sample `TaskSample9_1.exe`.

**These are separate memory captures. The two process trees and PIDs must not be treated as a single incident.**

The report contains evidence of injected-code indicators and a `HollowProcesses` alert. Findings are limited to what the original screenshots and student report support. Neither memory image nor malicious executable is distributed here.

## Investigation A: `ngentask.exe` and private executable memory

**SIT324 Task 8.3D, PDF pp. 211–219**

| Item | Documented observation |
| --- | --- |
| Memory source | `task8_memory.elf` captured from VirtualBox VM |
| Parent | `taskhostw.exe`, PID **2748** |
| Affected process | `ngentask.exe`, PID **5932** |
| Displayed executable path | `C:\Windows\Microsoft.NET\Framework\v4.0.30319\NGenTask.exe` |
| Plugins | `windows.info.Info`, `windows.pslist.PsList`, `windows.dlllist.DllList`, `windows.ldrmodules.LdrModules`, `windows.cmdline.CmdLine`, `windows.vadinfo.VadInfo`, `windows.malfind.Malfind` |

### Investigation steps

1. Capture the running virtual machine's memory using `VBoxManage debugvm ... dumpvmcore`.
2. Validate the dump with `windows.info.Info`.
3. Correlate `pslist` entries and `cmdline` to establish the PID and parent relationship.
4. Compare `dlllist` and `ldrmodules` to inspect loader-list membership and mapped paths.
5. Search `vadinfo` and `malfind` for private, executable memory without a normal file-backed mapping.

### Findings and interpretation

The report identifies loader-list mismatches in PID 5932. **Importantly, the main `ngentask.exe` executable path remains visible in `ldrmodules`.** The screenshot therefore **does not** support claiming a fully absent mapped executable path, and `InLoad/ InInit/ InMem=False` values alone are insufficient to prove hollowing.

The stronger indicators come from `vadinfo` and `malfind`, which show private `PAGE_EXECUTE_READWRITE` regions including:

- `0x1b70000–0x1b7ffff`
- `0x3f20000–0x3f2ffff`
- `0x7fc50000–0x7fc9ffff`
- `0x7fc40000–0x7fc4ffff`

**Assessment:** The report supports suspected injected code in `ngentask.exe` based on combined memory indicators. It does **not** conclusively demonstrate full process hollowing from the loader path alone.

### Source commands (historical report)

```powershell
python vol.py -f C:\Users\sit\Desktop\task8_memory.elf windows.pslist.PsList
python vol.py -f C:\Users\sit\Desktop\task8_memory.elf windows.ldrmodules.LdrModules --pid 5932
python vol.py -f C:\Users\sit\Desktop\task8_memory.elf windows.vadinfo.VadInfo --pid 5932
python vol.py -f C:\Users\sit\Desktop\task8_memory.elf windows.malfind.Malfind --pid 5932
```

These were used in the original Windows lab. They are **not** claimed to have been rerun while preparing this public portfolio.

## Investigation B: Guest memory capture and suspicious `svchost.exe`

**SIT324 Task 9.1P, PDF pp. 222–226**

| Item | Documented observation |
| --- | --- |
| Sample | `TaskSample9_1.exe` |
| Parent process | `TaskSample9_1.exe`, PID **2784** |
| Suspicious child | `svchost.exe`, PID **3176**, PPID **2784** |
| ProcWatch representation | PID `C68` (hex) = **3176** (decimal) |
| Reported child path | `C:\Windows\SysWOW64\svchost.exe` |
| Child current directory | `C:\malware_for_tasks\Task9_1P\` |
| Memory source | `memdump.mem`, captured using **FTK Imager** |
| Key plugins | `windows.pstree.PsTree`, `windows.malware.hollowprocesses.HollowProcesses` |

### Investigation steps

1. Launch ProcWatch and Process Explorer before executing the lab sample.
2. Observe newly spawned processes and record the candidate PID `C68` in ProcWatch.
3. Capture guest RAM with FTK Imager.
4. Convert `C68` from hexadecimal to decimal and correlate PID **3176** in Process Explorer.
5. Use Volatility `PsTree` to establish the relationship `TaskSample9_1.exe (2784) → svchost.exe (3176)`.
6. Use Volatility `HollowProcesses` to assess executable memory and loader-list protection anomalies.

### Findings

The Process Explorer evidence identifies `svchost.exe` as a 32-bit process running from the `SysWOW64` path. It also shows an unusual current working directory in the malware task folder.

The Volatility `PsTree` screenshot shows `TaskSample9_1.exe` (PID **2784**) creating `svchost.exe` (PID **3176**).

The `HollowProcesses` result then flags PID **3176**, including:

- Unexpected `PAGE_EXECUTE_READWRITE` protection for a VAD hosting the executable, with a **non-file-backed region**.
- Unexpected `PAGE_EXECUTE_READWRITE` protection associated with a DLL entry in the PEB's loader list.

**Assessment:** These correlated findings support the report's conclusion that the suspicious child exhibited **process hollowing indicators**. The plugin result alone cannot establish every execution step or the malicious payload's complete behaviour.

### Source commands (historical report)

```powershell
vol -f C:\malware_for_tasks\Task9_1P\memdump.mem windows.pstree.PsTree
vol -f C:\malware_for_tasks\Task9_1P\memdump.mem windows.malware.hollowprocesses.HollowProcesses
```

## Original screenshots

See [the evidence register](../../docs/memory-forensics-evidence-register.md) for image provenance, exact pages and what each screenshot proves.

## Proposed defensive follow-up

- Cross-check suspicious parent-child relationships with endpoint process telemetry.
- Investigate unexplained private executable VADs, especially with RWX permissions.
- Correlate loader-list mismatches with mapped-image, executable-path and module-signature evidence.
- Preserve memory and supporting endpoint logs before making remediation decisions.
- Triage false positives carefully because executable memory alone is not conclusive malware evidence.

These are **recommendations**, not controls implemented in the coursework.

## Reproducibility and safe publication

This repository contains a technical case study with source-page references and selected, sanitised original screenshot crops. The original memory dumps, malware binaries, complete university PDFs and private credentials are not published. Those raw artefacts are **not currently available for independent reproduction**.

No live malware execution was performed to prepare this public portfolio entry.

[View the portfolio case study](https://devv000-git.github.io/#project/memory-forensics)
