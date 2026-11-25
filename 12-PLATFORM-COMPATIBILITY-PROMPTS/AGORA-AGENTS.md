# PAW compatibility investigator — Agora Android target

Use `00-COMMON-FORENSIC-PROTOCOL.md` as the controlling protocol, then execute this platform-specific extension.

## Target boundary

Identify the exact Agora application package, app version, Android version, device or emulator, provider/model configuration, account mode, and network/privacy route visible to the tester. Do not substitute a generic Android app, provider API, or screenshot for an Agora application test.

## Android-specific probes

1. Verify installation and launch. Record package/version and device/emulator identity without personal data.
2. Test the real PAW import or file-open path using a harmless fixture. Record whether Markdown, JSON, directories, archives, and attachments are accepted and where they are stored.
3. Test core prompt use, one skill, one agent specification, one workflow procedure, and one schema separately. Distinguish display/readability from actual activation or execution.
4. Test provider configuration only with a non-sensitive test account or mock route. Never paste real secrets into screenshots, logs, or the PAW repository.
5. Test offline/online behaviour, app restart, project/archive continuity, and export/delete behaviour only when safe and reversible. Mark destructive or privacy-sensitive checks `BLOCKED` unless explicitly approved.
6. Capture screen recordings or screenshots with secrets and personal data redacted. Record manual steps precisely enough for a second tester to reproduce them.

## Required conclusion

Agora compatibility is Android-app-specific. Do not infer it from generic Markdown support, an API test, another Android build, or another provider. If no device/emulator and installed Agora build are available, report the native checks as `BLOCKED`.