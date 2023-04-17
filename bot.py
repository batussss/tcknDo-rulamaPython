import telegram.ext
from suds.client import Client
import datetime



token= "" #Your bot token 




def help(update,context):
    update.message.reply_text("""
                              
    Developed by Batuhan 
    batuddxd@gmail.com
    
    tckn-isim-soyisim-doğumyılı 
    
    *şeklinde yazarak bilgilerin doğru olup olmadığı ve 
    18yaşından büyük olup olmadığı doğrulanır*                             
                              
                              """)
                     
def handle_message(update,context):
   
    veri= update.message.text
    if veri.count('-')==3:
        res= veri.replace('-',' ')
        tcveri= res.split(' ')[0]
        isimveri= res.split(' ')[1]
        soyisimveri= res.split(' ')[2]
        yilveri=res.split(' ')[3] #str
        
        today = datetime.date.today()
        şuankiyil=today.year  #int

        try:
            pr= "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?op=TCKimlikNoDogrula&wsdl"
            client= Client(pr)
            resultwsdl = client.service.TCKimlikNoDogrula(tcveri,isimveri,soyisimveri,yilveri)
            print(resultwsdl)
        
            if resultwsdl==True:
                update.message.reply_text("Girilen kimlik bilgileri doğrudur.")
                yaş =şuankiyil-int(yilveri)
                print(yaş)
                if yaş >=	18:
                    update.message.reply_text("Vatandaş 18 ve üstü yaşındadır. Yaş:"+str(yaş))
                else:
                    update.message.reply_text("Vatandaş 18 yaşından küçüktür. Yaş:"+str(yaş))

            else:
                update.message.reply_text("Girilen kimlik bilgileri yanlışdır.")
        except:
            update.message.reply_text("Yazdığınız değerleri tekrar kontrol edin ")

    else:
        update.message.reply_text("lütfen istenilen biçimde veri girin yardım için /help")

    





updater=telegram.ext.Updater(token, use_context=True)
disp=updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("help",help))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))


updater.start_polling()
updater.idle()