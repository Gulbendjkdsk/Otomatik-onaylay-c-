import telebot

# Bot Token
TOKEN = "7933734810:AAHX6ObQmnFDgDXnBGtxL9WgltQlRs0slTA"
bot = telebot.TeleBot(TOKEN)

# Grup ID
GROUP_ID = -1002320628068  

@bot.chat_join_request_handler()
def approve_request(request):
    user = request.from_user
    bot.approve_chat_join_request(GROUP_ID, user.id)

    # Konsola mesaj yazdır
    print(f"✅ {user.first_name} ({user.id}) gruba alındı.")

    # Gruba duyuru mesajı gönder
    bot.send_message(GROUP_ID, f"✅ {user.first_name} gruba katıldı hoş geldin dostum. ")

print("Bot çalışıyor...")
bot.polling()