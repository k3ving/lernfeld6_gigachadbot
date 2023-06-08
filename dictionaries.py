import answer as ans

answers = {
    "Start": ans.Answer("Hallo ich bin der Chatbot. Mit welchem Problem kann ich Ihnen weiterhelfen?", ["Software", "Hardware", "Netzwerk", "Datensicherheit", "Authentifikation", "Andere"]),
    "Software": ans.Answer("Ein Software Problem? Welche der folgenden Dinge trifft zu?", ["Programm abgestürzt", "Update Problem", "Bug", "Programm ist langsam", "Anderes"]),
    "Hardware": ans.Answer("Ein Hardware Problem? Welche der folgenden Dinge trifft zu?", ["Computerabsturz", "Serverabsturz", "Druckerproblem", "Physische Schaeden", "Anderes"]),
    "Netzwerk": ans.Answer("Ein Netzwerk Problem? Welche der folgenden Dinge trifft zu?", ["Schlechte Verbindung", "Webseiten Probleme", "Verbindungsprobleme", "Anderes"]),
    "Datensicherheit": ans.Answer("Ein Datensicherheit Problem? Welche der folgenden Dinge trifft zu?", ["Hacking Probleme", "Firewall Detection", "Anderes"]),
    "Authentifikation": ans.Answer("Ein Authentifikation Problem? Welche der folgenden Dinge trifft zu?", ["Passwort vergessen", "Anderes"])
    "Anderes": ans.Answer("Ich rate Ihnen sich an unser Support-Team zu wenden, bitte wählen sie eine der Kontaktoptionen.", ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
}
