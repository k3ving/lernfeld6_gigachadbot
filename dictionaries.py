from answer import *

answers = {
    "Start": Answer("Hallo ich bin der Chatbot. Mit welchem Problem kann ich Ihnen weiterhelfen?", ["Software", "Hardware", "Netzwerk", "Datensicherheit", "Authentifikation", "Andere"]),
    "Software": Answer("Ein Software Problem? Welche der folgenden Dinge trifft zu?", ["Programm abgestürzt", "Update Problem", "Bug", "Programm ist langsam", "Anderes"]),
        "Programm abgestürzt": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Programm hängt immer noch"]),
            "Programm hängt immer noch": Answer("Ich rate Ihnen das Sie unser Support-Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
        "Update Problem": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Update hängt immer noch"]),
            "Update hängt immer noch": Answer("Ich rate Ihnen das Sie unser Support-Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
        "Bug": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Bug bleibt bestehen"]),
            "Bug bleibt bestehen": Answer("Ich rate Ihnen das Sie unser Support-Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
        "Programm ist langsam": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?" , ["Funktioniert wieder", "Programm bleibt langsam"]),
            "Programm bleibt langsam": Answer("Liegt ein Update für das Programm vor?" , ["Funktioniert wieder", "Funktioniert nicht"]),
                "Funktioniert nicht": Answer("Ich rate Ihnen das Sie unser Support-Team kontaktieren." , ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
    
    "Hardware": Answer("Ein Hardware Problem? Welche der folgenden Dinge trifft zu?", ["Computerabsturz", "Serverabsturz", "Druckerproblem", "Physische Schaeden", "Anderes"]),
        "Computerabsturz": Answer("Können Sie den PC ausschalten/neustarten? Forcieren Sie indem Sie den An/Aus-Knopf gedrückt halten.", ["Funktioniert wieder", "Neustart funktioniert nicht"]),
            "Neustart funktioniert nicht": Answer("Ihr PC hat womöglich einen schweren Defekt. Ich rate Ihnen das Sie Ihren Diensleister kontaktieren.", ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
        "Serverabsturz": Answer("Ich bitte Sie unverzüglich unser Support Team zu kontaktieren", ["Zum Mitarbeiter weiterleiten", "Ticket erstellen"]),
        "Druckerproblem": Answer("Gibt der Drucker einen Fehlercode an oder leuchtet er in einer bestimmten Weise?", ["Ja der Drucker macht etwas", "Nein der Drucker macht nichts"]), 
            "Ja der Drucker macht etwas": Answer("Ich rate Ihnen das Sie unser Support-Team kontaktieren.", [, ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
            "Nein, der Drucker macht nichts": Answer("Taucht das Gerät im Geräte-Manager auf? Wenn ja trennen Sie den Drucker 10-15 Minuten vom Strom", ["Druckerproblem bleibt bestehen", "Funktioniert wieder"]), 
                "Druckerproblem bleibt bestehen": Answer("Ich rate Ihnen das Sie unser Support-Team kontaktieren.", ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),                                                                                            
        "Physische Schaeden": Answer("Ich rate Ihnen das Sie unser Support Team kontaktieren.", ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
                                                                                                             
    "Netzwerk": Answer("Ein Netzwerk Problem? Welche der folgenden Dinge trifft zu?", ["Webseiten Probleme", "Verbindungsprobleme", "Anderes"]),
    "Datensicherheit": Answer("Ein Datensicherheit Problem? Welche der folgenden Dinge trifft zu?", ["Hacking Probleme", "Firewall Detection", "Anderes"]),
    "Authentifikation": Answer("Ein Authentifikation Problem? Welche der folgenden Dinge trifft zu?", ["Passwort vergessen", "Anderes"])
    "Anderes": Answer("Ich rate Ihnen sich an unser Support-Team zu wenden, bitte wählen sie eine der Kontaktoptionen.", ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
    "Zum Mitarbeiter weiterleiten": Answer("Bitte wählen Sie die Nummer 01234567890 um mit einem unserer Mitarbeiter in Verbindung zu treten"),
    "Gespräch abbrechen": Answer("Alles klar, Sie können uns unter 01234567890 oder unter der Mail info@firma.de erreichen wenn Sie es sich anders überlegen"),
    "Ticket erstellen": Answer("Ein Ticket mit Ihrem Problem wurde erstellt, ein Mitarbeiter wird sich dann mit Ihnen in Verbindung setzen"),
    "Funktioniert wieder": Answer("Freut mich das Ich Ihnen helfen konnte."),                                 
}
