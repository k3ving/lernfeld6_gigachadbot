import answer as ans

answers = {
    "Start": ans.Answer("Hallo ich bin der Chatbot. Mit welchem Problem kann ich Ihnen weiterhelfen?", ["Software", "Hardware", "Netzwerk", "Datensicherheit", "Authnetifikation"]),
    "Absturz": ans.Answer("Ein Absturz. Welche der folgenden Dinge trifft zu?", ["Programm friert ein", "Lädt endlos", "Programm schließt sich"]),
    "Problem bei Login": ans.Answer("Probleme beim Login. Was trifft am ehesten zu?", ["Falscher Nutzername", "Falsche Email", "Falsches Passwort"]),
    "Falscher Nutzername": ans.Answer("Kontaktieren Sie bitte unser Support Team.", ["Danke!"]),
    "Falsche Email": ans.Answer("Kontaktieren Sie bitte unser Support Team.", ["Danke!"]),
    "Falsches Passwort": ans.Answer("Bitte versuchen Sie Ihr Passwort zurückzusetzen.", ["Danke!"])
}
