# Unity Editor external refresh

`DownfallExternalRefresh` is a shared Editor-only fallback for requesting an Asset Database refresh while another application has focus. It does not provide general remote control. The Unity Editor must already be open and the tool must have been compiled at least once.

Create an empty file at `UnityProject/Temp/DownfallExternalRefresh.request` to request a refresh. The Editor consumes the file and logs `DOWNFALL_EXTERNAL_REFRESH: request received`. It defers requests while Play Mode is active or changing, or while the Editor is compiling or updating. Unity's `Temp` directory is ignored by Git and is not persistent; if the Editor exits or the request is lost, submit a new request after it reopens.

The request is local and has no payload. File access failures are logged. A received log message confirms the request was accepted, not that every resulting compile or import succeeded: inspect the Unity console and relevant tests separately. Do not change an open scene asset externally while it has unsaved Editor changes.

Unity Pipeline is a separate, optional integration and is not required by this tool. Its package and the current Assistant-related settings remain subject to separate project review.
