from answer import *

end_options_default = ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]

answers = {
    "Start": Answer("Hallo, ich bin der Chatbot. Bei welchem Problem kann ich Ihnen weiterhelfen?", ["Software", "Hardware", "Netzwerk", "Datensicherheit", "Authentifikation", "Anderes"]),
    "Software": Answer("Ein Software Problem? Welches der folgenden Dinge trifft zu?", ["Programm abgestürzt", "Update Problem", "Bug", "Programm ist langsam", "Anderes"]),
        "Programm abgestürzt": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?", ["Funktioniert wieder", "Programm hängt immer noch"]),
            "Programm hängt immer noch": Answer("Ich rate Ihnen, dass Sie unser Support-Team kontaktieren.", ["Zum Mitarbeiter weiterleiten", "Gespräch abbrechen", "Ticket erstellen"]),
        "Update Problem": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?", ["Funktioniert wieder", "Update hängt immer noch"]),
            "Update hängt immer noch": Answer("Ich rate Ihnen, dass Sie unser Support-Team kontaktieren.", end_options_default),
        "Bug": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?", ["Funktioniert wieder", "Bug bleibt bestehen"]),
            "Bug bleibt bestehen": Answer("Ich rate Ihnen, dass Sie unser Support-Team kontaktieren.", end_options_default),
        "Programm ist langsam": Answer("Haben Sie versucht das Programm oder Ihren Rechner neuzustarten?", ["Funktioniert wieder", "Programm bleibt langsam"]),
            "Programm bleibt langsam": Answer("Liegt ein Update für das Programm vor?", ["Funktioniert wieder", "Funktioniert nicht"]),
                "Funktioniert nicht": Answer("Ich rate Ihnen, dass Sie unser Support-Team kontaktieren.", end_options_default),
    
    "Hardware": Answer("Ein Hardware Problem? Welches der folgenden Dinge trifft zu?", ["Computerabsturz", "Serverabsturz", "Druckerproblem", "Physische Schaeden", "Anderes"]),
        "Computerabsturz": Answer("Können Sie den PC ausschalten/neustarten? Forcieren Sie indem Sie den An/Aus-Knopf gedrückt halten.", ["Funktioniert wieder", "Neustart funktioniert nicht"]),
            "Neustart funktioniert nicht": Answer("Ihr PC hat womöglich einen schweren Defekt. Ich bitte Sie unverzüglich unser Support-Team zu kontaktieren", end_options_default),
        "Serverabsturz": Answer("Ich bitte Sie unverzüglich unser Support-Team zu kontaktieren.", ["Zum Mitarbeiter weiterleiten", "Ticket erstellen"]),
        "Druckerproblem": Answer("Gibt der Drucker einen Fehlercode an oder leuchtet er in einer bestimmten Weise?", ["Ja, der Drucker macht etwas", "Nein, der Drucker macht nichts"]), 
            "Ja, der Drucker macht etwas": Answer("Ich rate Ihnen, dass das Sie unser Support-Team kontaktieren.", end_options_default),
            "Nein, der Drucker macht nichts": Answer("Taucht das Gerät im Geräte-Manager auf? Wenn ja, trennen Sie den Drucker 10-15 Minuten vom Strom.", ["Druckerproblem bleibt bestehen", "Funktioniert wieder"]),
                "Druckerproblem bleibt bestehen": Answer("Ich rate Ihnen, dass Sie unser Support-Team kontaktieren.", end_options_default),
        "Physische Schaeden": Answer("Ich rate Ihnen, dass Sie unser Support Team kontaktieren.", end_options_default),
                                                                                                             
    "Netzwerk": Answer("Ein Netzwerk Problem? Welches der folgenden Dinge trifft zu?", ["Webseiten Probleme", "Verbindungsprobleme", "Anderes"]),
        "Webseiten Probleme": Answer("Können sie sicherstellen das Ihre Internet Verbindung besteht?", ["Verbindung steht", "Verbindung steht nicht"]),
            "Verbindung steht nicht": Answer("Ich rate Ihnen, dass Sie unser Support-Team kontaktieren.", end_options_default),
            "Verbindung steht": Answer("Sind auch andere Webseiten betroffen?", ["Ja, auch andere", "Nein, keine anderen"]),                                                                                                
                "Ja, auch andere": Answer("Ich rate Ihnen, dass Sie unser Support-Team kontaktieren.", end_options_default),
                "Nein, keine anderen" : Answer("Ist die Webseite eine interne Ihrer Firma oder die einer externen?", ["Intern", "Extern"]),
                    "Extern": Answer("Der Webseiten Inhaber hat womöglich Konnektivitätsprobleme, kontaktieren Sie Ihn wenn möglich.", []),
                    "Intern": Answer("Ich rate Ihnen, dass Sie unser Support-Team kontaktieren.", end_options_default),
        "Verbindungsprobleme": Answer("Wo befinden Sie sich?", ["Unterwegs", "Firma", "Homeoffice"]),
            "Unterwegs": Answer("Wie zum Henker schaffen Sie es dann sich mit dem Chatbot zu verbinden?", []),
            "Firma": Answer("Ich bitte Sie unverzüglich unser Support-Team zu kontaktieren.", ["Zum Mitarbeiter weiterleiten", "Ticket erstellen"]),
            "Homeoffice": Answer("Prüfen Sie Ihre Internetverbindung, wenn diese nicht funktioniert trennen Sie Ihren Router vom Strom für 5-10 Minuten.", ["Verbindung geht nicht", "Funktioniert wieder"]),                                                                                               
                   "Verbindung geht nicht": Answer("Bitte kontaktieren Sie Ihren Provider und prüfen, ob es Störungen in Ihrer Gegend gibt.", []),
                                                                                                             
    "Datensicherheit": Answer("Ein Datensicherheits Problem? Welches der folgenden Dinge trifft zu?", ["Hacking Probleme", "Firewall Detection", "Anderes"]),
        "Meldung": Answer("Haben Sie eine Meldung bekommen?", ["Ich habe eine Meldung bekommen", "Ich habe keine Meldung bekommen"]),
            "Ich habe eine Meldung bekommen": Answer("Welche der folgenden Meldungen trat auf?", ["Ein Update ist verfügbar", "Ihre Sicherheit ist kompromittiert", "Verdächtige Aktivitäten"]),
                "Ein Update ist verfügbar": Answer("Soll ich das dem Support-Team mitteilen?", end_options_default),
                "Ihre Sicherheit ist kompromittiert": Answer("Ich bitte Sie unverzüglich unser Support-Team zu kontaktieren.", ["Zum Mitarbeiter weiterleiten", "Ticket erstellen"]),
                "Verdächtige Aktivitäten": Answer("Ich bitte Sie unverzüglich unser Support-Team zu kontaktieren.", ["Zum Mitarbeiter weiterleiten", "Ticket erstellen"]),
            "Ich habe keine Meldung bekommen": Answer("Ich bitte Sie unverzüglich unser Support-Team zu kontaktieren.", ["Zum Mitarbeiter weiterleiten", "Ticket erstellen"]),
                                                                                                             
    "Authentifikation": Answer("Ein Authentifikation Problem? Welche der folgenden Dinge trifft zu?", ["Passwort vergessen", "Anderes"]),
        "Passwort vergessen": Answer("Alles klar! Folgen sie diesem Link, um Ihr Passwort zurückzusetzen: https://firma.de/password_reset", []),
                                                                                                             
    "Anderes": Answer("Ich rate Ihnen sich an unser Support-Team zu wenden, bitte wählen sie eine der Kontaktoptionen.", end_options_default),
    "Zum Mitarbeiter weiterleiten": Answer("Bitte wählen Sie die Nummer 01234567890 um sich mit einem unserer Mitarbeiter in Verbindung zu setzen, Tschuess und schoenen Tag noch.", []),
    "Gespräch abbrechen": Answer("Alles klar, Sie können uns unter 01234567890 oder unter der Mail info@firma.de erreichen wenn Sie es sich anders überlegen, Tschuess und schoenen Tag noch.", []),
    "Ticket erstellen": Answer("Ein Ticket mit Ihrem Problem wurde erstellt, ein Mitarbeiter wird sich dann mit Ihnen in Verbindung setzen, Tschuess und schoenen Tag noch.", []),
    "Funktioniert wieder": Answer("Freut mich das Ich Ihnen helfen konnte, Tschuess und schoenen Tag noch.", []),
}
