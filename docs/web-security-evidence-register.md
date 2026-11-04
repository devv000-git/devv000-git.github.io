# SIT379 Web Application Security Evidence Register

## Provenance

Original university portfolio: **SIT379 Ethical Hacking**. Task 8.1P appears on PDF pages **224–237** and Task 8.2C on pages **240–255**. The exercises used the intentionally vulnerable **BodgeIt Store** and **DVWA** applications.

The site publishes four cropped, high-contrast copies of evidence already embedded in the PDF. The original source pages remain private.

| Evidence | PDF page | Directly demonstrated | Limit |
| --- | --- | --- | --- |
| [reflected-xss.png](../assets/evidence/web-security/reflected-xss.png) | **228**, Figure 3 | Browser alert appeared after submitting script input into a search workflow | Does not show impact beyond execution of the test script |
| Registration screenshots | **229**, Figures 4–5 | Browser alert and registration confirmation after payload submission | Persistence inferred from the workflow and written report |
| SQL-injection login | **230**, Figure 6 | Login success after an injected username condition | Application is deliberately vulnerable |
| Password change GET (BodgeIt Store) | **246**, Figure 5 | Burp Repeater HTTP 200 response and password-change confirmation | Does not show a production deployment |
| [basket-result.png](../assets/evidence/web-security/basket-result.png) | **249**, Figure 8 | Basic Widget quantity **-15** and basket total **($4.00)** | Test shopping basket only |
| [upload-mime.png](../assets/evidence/web-security/upload-mime.png) | **252**, Figure 11 | Multipart upload request identified an HTML filename while claiming image/jpeg Content-Type | Request alone does not demonstrate successful upload |
| [upload-confirmation.png](../assets/evidence/web-security/upload-confirmation.png) | **253**, Figure 12 | DVWA reports the uploaded file was accepted | An isolated DVWA lab |
| HTML rendered | **254**, Figure 13 | Uploaded HTML message displayed when opened | Not evidence of OS command execution or a remote shell |

### Additional activities not shown in the cropped screenshot gallery

The complete SIT379 Task 8.1P report also includes diagnostic data exposure (p. 226), a DVWA command-execution and shell demonstration as the restricted web-server user (pp. 232–233), and a separate PHP upload and file-inclusion chain (pp. 234–235). These are presented only as retrospective university-lab observations, with no payloads or attack scripts distributed.

The command execution and PHP upload chain are separate from the later **plain HTML** upload test on pp. 251–254. Do not interpret a browser-rendered HTML heading as evidence of server-side code execution.

### Publication decisions

The GET password-change screenshots on pp. 244–246 include sample passwords and session-cookie values, so they have not been published in this gallery. Their outcomes remain described with source-page references.

## Important interpretation

The portfolio distinguishes **what was directly observed** from **what was concluded**. In particular, the uploaded HTML file rendering in the browser does not prove server-side code execution, even though the university narrative uses the phrase “script executed.”

## Publication and safety

Screenshot excerpts contain only controlled training applications. The complete university submission, student identifiers and potentially sensitive materials are not published. The case study describes vulnerabilities at an analytical level and links to remediation guidance without distributing an automated attack tool.
