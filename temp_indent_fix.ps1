$path = 'c:\_\me\bible\Defenders\github\defenders\md\Trinity\HolySpirit.Slides.md'
$text = Get-Content -Raw -Encoding UTF8 $path
$lines = $text -split "`r`n", -1
for ($i = 0; $i -lt $lines.Length; $i++) {
    $line = $lines[$i]
    if ($line -match '^( +)(\*|\-|\+|\d+\.)\s') {
        $indent = $matches[1].Length
        if ($indent -ge 4 -and ($indent % 4 -eq 0)) {
            $newIndent = ' ' * ($indent / 2)
            $lines[$i] = $newIndent + $line.Substring($indent)
        }
    }
}
$out = ($lines -join "`r`n")
Set-Content -Encoding UTF8 -NoNewline -Path $path -Value $out