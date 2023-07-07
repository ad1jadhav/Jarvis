import text_to_speech   
import speech_to_text 
import datetime
import webbrowser

def Action(data):  
    user_data = data.lower()

    if "what is your name" in user_data :
        text_to_speech.text_to_speech("My name is jarvis and i am your personal virtual assistant") 
        return "My name is jarvis and i am your personal virtual assistant"


    elif "hello jarvis" in user_data or "hey jarvis" in user_data : 
        text_to_speech.text_to_speech("hello, mr.aditya, How can i help you")
        return "Hello, mr.aditya, How can i help you"
    
    elif "good morning" in user_data : 
        text_to_speech.text_to_speech("very good morning mr.aditya")     
        return "Very good morning mr.aditya"     
    
    elif "time now" in user_data : 
        current_time = datetime.datetime.now() 
        Time = (str(current_time)) + " Hour :", (str(current_time.minute)) + "Minute" 
        text_to_speech.text_to_speech(Time) 
        return Time
    
    elif "shutdown" in user_data : 
        text_to_speech.text_to_speech("ok mr.aditya") 
        return "ok mr.aditya"  
    
    elif "play music" in user_data :
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is ready to play mr.aditya") 
        return "gaana.com is ready to play mr.aditya"    
    
    elif "open youtube" in user_data :
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com has been opend mr.aditya") 
        return "youtube.com has been opend mr.aditya"
    
    elif "open google" in user_data :
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com has been opend mr.aditya")
        return "google.com is ready to play mr.aditya" 
    
    elif "open wikipedia" in user_data :
        webbrowser.open("https://wikipedia.com/")
        text_to_speech.text_to_speech("wikipedia.com has been opend mr.aditya")
        return "wikipedia.com is ready to play mr.aditya"
    
    elif "shahrukh khan" in user_data :
        webbrowser.open("https://en.wikipedia.org/wiki/Shah_Rukh_Khan")
        text_to_speech.text_to_speech("Shahrukh khan, is an Indian actor and film producer who works in Hindi films. Referred to in the media as the Baadshah of Bollywood and King Khan")
        return "Shahrukh khan, is an Indian actor and film producer who works in Hindi films. Referred to in the media as the Baadshah of Bollywood and King Khan"
    
    elif "harry potter" in user_data :
        webbrowser.open("https://en.wikipedia.org/wiki/Harry_Potter")
        text_to_speech.text_to_speech("Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling")
        return "Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling"   
    
    elif "dada kondke" in user_data :
        webbrowser.open("https://en.wikipedia.org/wiki/Dada_Kondke")
        text_to_speech.text_to_speech("Here is the information about Dada Kondke.")
        return "Here is the information about Dada Kondke."
    
    elif "iron man helmet" in user_data :
        webbrowser.open("https://www.amazon.in/Wearable-Electric-Children-Halloween-Masquerade/dp/B09TP5N341/ref=sr_1_7?adgrpid=140166493333&hvadid=617893956650&hvdev=c&hvlocphy=9062117&hvnetw=g&hvqmt=b&hvrand=18093926079842906579&hvtargid=kwd-302641328344&hydadcr=25673_2638571&keywords=metal+iron+man+helmet&qid=1684652139&sr=8-7/")
        text_to_speech.text_to_speech("here you can buy ironman helmet mr.aditya")
        return "here you can buy ironman helmet mr.aditya"   
    
    elif "novels" in user_data :
        webbrowser.open("https://www.amazon.in/Harry-Potter-Complete-Collection-Rowling/dp/B01GFJTI20/ref=sr_1_5?adgrpid=127082651722&ext_vrnc=hi&hvadid=537076437812&hvdev=c&hvlocphy=9062117&hvnetw=g&hvqmt=b&hvrand=2350959680055642334&hvtargid=kwd-298479130241&hydadcr=15728_1974079&keywords=harry+potter+book+complete+set&qid=1684652569&sr=8-5/")
        text_to_speech.text_to_speech("here you can buy harry potter novels mr.aditya")
        return "here you can buy harry potter novels mr.aditya"   
    
    else :
        text_to_speech.text_to_speech("sorry, mr. aditya but the given command is not under my system")     
        return "sorry, mr. aditya but the given command is not under my system"  


    
         
    
          
    
      
    