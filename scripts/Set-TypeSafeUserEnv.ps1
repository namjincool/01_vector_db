[CmdletBinding()]
param(
    [string]$EnvFile = (Join-Path $PSScriptRoot "..\\.env")
)

$resolvedEnvFile = Resolve-Path -LiteralPath $EnvFile -ErrorAction Stop
$settings = @{}

foreach ($line in Get-Content -LiteralPath $resolvedEnvFile) {
    $trimmed = $line.Trim()
    if (-not $trimmed -or $trimmed.StartsWith("#")) { continue }

    if ($trimmed -match "^(TYPESAFE_API_KEY|TYPESAFE_MODEL|TYPESAFE_ENDPOINT)=(.*)$") {
        $value = $matches[2].Trim()
        if ($value.Length -ge 2 -and (
            ($value.StartsWith('"') -and $value.EndsWith('"')) -or
            ($value.StartsWith("'") -and $value.EndsWith("'"))
        )) {
            $value = $value.Substring(1, $value.Length - 2)
        }
        $settings[$matches[1]] = $value
    }
}

$apiKey = $settings["TYPESAFE_API_KEY"]
if ([string]::IsNullOrWhiteSpace($apiKey) -or $apiKey -eq "replace-with-your-typesafe-api-key") {
    throw "Set a real TYPESAFE_API_KEY in $resolvedEnvFile before registering it globally."
}

$model = $settings["TYPESAFE_MODEL"]
if ([string]::IsNullOrWhiteSpace($model)) { $model = "jev-latest" }

# User scope affects future terminals and apps for this Windows account only.
[Environment]::SetEnvironmentVariable("TYPESAFE_API_KEY", $apiKey, "User")
[Environment]::SetEnvironmentVariable("TYPESAFE_MODEL", $model, "User")

if ($settings.ContainsKey("TYPESAFE_ENDPOINT") -and -not [string]::IsNullOrWhiteSpace($settings["TYPESAFE_ENDPOINT"])) {
    [Environment]::SetEnvironmentVariable("TYPESAFE_ENDPOINT", $settings["TYPESAFE_ENDPOINT"], "User")
}

Write-Output "Registered TypeSafe settings for the current Windows user."
Write-Output "TYPESAFE_API_KEY: [redacted]"
Write-Output "TYPESAFE_MODEL: $model"
if ($settings.ContainsKey("TYPESAFE_ENDPOINT") -and -not [string]::IsNullOrWhiteSpace($settings["TYPESAFE_ENDPOINT"])) {
    Write-Output "TYPESAFE_ENDPOINT: configured"
}
Write-Output "Open a new terminal or restart the application to use the persistent values."

