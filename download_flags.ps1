$flags = @{
    "dk" = "https://flagcdn.com/w40/dk.png"
    "gb" = "https://flagcdn.com/w40/gb.png"
    "nl" = "https://flagcdn.com/w40/nl.png"
    "de" = "https://flagcdn.com/w40/de.png"
    "no" = "https://flagcdn.com/w40/no.png"
    "se" = "https://flagcdn.com/w40/se.png"
    "es" = "https://flagcdn.com/w40/es.png"
    "fr" = "https://flagcdn.com/w40/fr.png"
    "it" = "https://flagcdn.com/w40/it.png"
    "fi" = "https://flagcdn.com/w40/fi.png"
}

foreach ($flag in $flags.GetEnumerator()) {
    $outFile = "static/images/flags/$($flag.Key).png"
    Invoke-WebRequest -Uri $flag.Value -OutFile $outFile
}
