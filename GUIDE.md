Attempted to install Go: An initial attempt was made to install Go using the webi installer (curl -sS https://webi.sh/golang | sh). However, the output indicated that Go was already installed.

Attempted to install Boot.dev CLI (failed): The command go install github.com/bootdotdev/bootdev@latest was executed, but it failed because the go command was not found in the system's PATH.

Identified Go executable path: You provided the output of which go, which showed the Go executable is located at /home/user/.local/opt/go/bin/go.

Confirmed Go executable existence and permissions: The command ls -l /home/user/.local/opt/go/bin/go confirmed that the Go executable exists at the specified path and has execute permissions.

Installed Boot.dev CLI using the full path: Since adding the Go directory to the PATH was not working as expected in the terminal session, the go install command was run by providing the full path to the go executable: /home/user/.local/opt/go/bin/go install github.com/bootdotdev/bootdev@latest. This command successfully downloaded and installed the Boot.dev CLI.

Verified Boot.dev CLI installation: The command $HOME/go/bin/bootdev --version was used to verify that the Boot.dev CLI was installed correctly and was accessible.

Logged in to Boot.dev CLI: The command $HOME/go/bin/bootdev login was executed to authenticate with your Boot.dev account.
