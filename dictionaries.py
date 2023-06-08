from answer import *

answers = {
    "Start": Answer("Hallo ich bin der Chatbot. Mit welchem Problem kann ich Ihnen weiterhelfen?", ["Software", "Hardware", "Netzwerk", "Datensicherheit", "Authentifikation", "Andere"]),
    "Software": Answer("Ein Software Problem? Welche der folgenden Dinge trifft zu?", ["Programm abgestürzt", "Update Problem", "Bug", "Programm ist langsam", "Anderes"]),
        "Programm abgestürzt": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Programm hängt immer noch"])
            "Programm hängt immer noch": Answer("Ich rate Ihnen das Sie unser Support Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"])
        "Update Problem": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Update hängt immer noch"])
            "Update hängt immer noch": Answer("Ich rate Ihnen das Sie unser Support Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"])
        "Bug": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Bug bleibt bestehen"])
            "Bug bleibt bestehen": Answer("Ich rate Ihnen das Sie unser Support Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"])
        "Programm ist langsam": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Programm bleibt langsam"])
            "Programm bleibt langsam": Answer("Liegt ein Update für das Programm vor?" , ["Funktioniert wieder", "Funktioniert nicht"])
                "Funktioniert nicht": Answer("Ich rate Ihnen das Sie unser Support Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"])
    
    "Hardware": Answer("Ein Hardware Problem? Welche der folgenden Dinge trifft zu?", ["Computerabsturz", "Serverabsturz", "Druckerproblem", "Physische Schaeden", "Anderes"]),
    "Netzwerk": Answer("Ein Netzwerk Problem? Welche der folgenden Dinge trifft zu?", ["Webseiten Probleme", "Verbindungsprobleme", "Anderes"]),
    "Datensicherheit": Answer("Ein Datensicherheit Problem? Welche der folgenden Dinge trifft zu?", ["Hacking Probleme", "Firewall Detection", "Anderes"]),
    "Authentifikation": Answer("Ein Authentifikation Problem? Welche der folgenden Dinge trifft zu?", ["Passwort vergessen", "Anderes"])
    "Anderes": Answer("Ich rate Ihnen sich an unser Support-Team zu wenden, bitte wählen sie eine der Kontaktoptionen.", ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
    "Programm abgestürzt": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Programm hängt immer noch"])
    "Update Problem": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Update hängt immer noch"])
    "Bug": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Bug bleibt bestehen"])
    "Programm ist langsam": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Programm bleibt langsam"])
    "Programm bleibt langsam": Answer("Liegt ein Update für das Programm vor?" , ["Funktioniert wieder", "Funktioniert nicht"])
    "Programm hängt immer noch": Answer("Ich rate Ihnen das Sie unser Support Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"])
    "Update hängt immer noch": Answer("Ich rate Ihnen das Sie unser Support Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"])
    "Bug bleibt bestehen": Answer("Ich rate Ihnen das Sie unser Support Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"])
    "Funktioniert nicht": Answer("Ich rate Ihnen das Sie unser Support Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"])
}
