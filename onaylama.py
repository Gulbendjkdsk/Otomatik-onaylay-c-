
import telebot

# Bot Token
TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

# Grup ID
GROUP_ID = -1002320628068  

@bot.chat_join_request_handler()
def approve_request(request):
    user = request.from_user
    
    try:
        # Kullanıcının grup durumunu kontrol et
        member = bot.get_chat_member(GROUP_ID, user.id)
        
        if member.status in ["member", "administrator", "creator"]:
            print(f"⚠ {user.first_name} ({user.id}) zaten grupta!")
        else:
            bot.approve_chat_join_request(GROUP_ID, user.id)
            print(f"✅ {user.first_name} ({user.id}) gruba alındı.")
            bot.send_message(GROUP_ID, f"✅ {user.first_name} gruba katıldı, hoş geldin dostum!")

    except telebot.apihelper.ApiException as e:
        print(f"Hata oluştu: {e}")

print("Bot çalışıyor...")
bot.polling()