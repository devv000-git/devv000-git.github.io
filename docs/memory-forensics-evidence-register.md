# Evidence register: Windows memory forensic investigations

**Unit:** SIT324 Malware Analysis, Deakin University (2026)  
**Original documentation:** Private university portfolio report  
**Exercises:** Task 8.3D (pp. 211–219) and Task 9.1P (pp. 222–226)

These are **different memory images from different lab tasks** and their evidence is not combined into one incident.

## Investigation A: `ngentask.exe` (PID 5932)

| Source PDF page | Figure | Documented technical evidence | Assessment |
| --- | --- | --- | --- |
| **211** | Figure 1 | VirtualBox memory dump `task8_memory.elf` | Establishes source acquisition |
| **213** | Figure 4 | `pslist`: `ngentask.exe` PID 5932, PPID 2748 | Identifies process relationship |
| **214** | Figure 6 | `ldrmodules`: module-list mismatches; **mapped main executable path is visible** | Mismatches justify investigation but do not by themselves prove hollowing |
| **216–217** | Figures 10 and 12 | `vadinfo`: private regions with executable memory permissions | Supports suspected injected code |
| **218** | Figure 14 | `malfind`: PID 5932 and private RWX regions | Strongest injected-code indicator in the source |

**Critical qualification:** The report explicitly corrects an earlier interpretation. A visible mapped path for the primary `ngentask.exe` image means the `ldrmodules` screenshot must **not** be described as showing a completely missing executable path. The final source assessment is **process injection indicators**, with hollowing checks documented, not a proven replacement of the main mapped image.

## Investigation B: `svchost.exe` (PID 3176)

| Source PDF page | Figure | Documented technical evidence | Assessment |
| --- | --- | --- | --- |
| **222** | Figure 1 | ProcWatch records newly created processes, PID `C68` | Candidate identified |
| **222–223** | Figure 2 | FTK Imager acquires guest memory `memdump.mem` | Establishes capture |
| **223** | Figure 3 | Calculator conversion `C68` hex = 3176 decimal | PID correlation |
| **224** | Figure 4 | Process Explorer properties for `svchost.exe` PID 3176 | Path, parent and current directory |
| **225** | Figure 5 | Volatility `PsTree`: parent `TaskSample9_1.exe` PID 2784 and child `svchost.exe` PID 3176 | Supports process ancestry |
| **225** | Figure 6 | Volatility `HollowProcesses`: RWX, non-file-backed executable VAD and suspicious loader entry | Supports hollowing indicators |

**Qualification:** The source report concludes this process was hollowed. The available screenshot directly records a `HollowProcesses` flag and unusual memory permissions. Further forensic validation would normally include inspecting the region contents, on-disk executable, and execution telemetry.

## Publication standard

Original screenshot crops are taken from the embedded figures, not recreated terminal text. They may be cropped and converted to high-contrast monochrome for legibility, but their commands, PIDs, plugin results and memory addresses are not rewritten.

No samples, raw volatile memory, credentials, student IDs or full university reports are published.

## Scope and limits

The case study is retrospective and source-based. It does **not** imply that the memory images or suspicious malware were newly executed, analysed or independently verified while building the public website.
