# PowerShell Script to get all .exe files opened in the past day
$startTime = (Get-Date).AddDays(-1)
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4688
    StartTime = $startTime
} | ForEach-Object {
    if ($_ | Select-String -Pattern ".exe") {
        $_.Properties[8].Value
    }
}