from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

bot = commands.Bot(command_prefix='/')

token = os.environ['DISCORD_BOT_TOKEN']

CHANNEL_ID =709712529613389875  #チャンネルID


# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    
    if now == '04:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('［@SWAP］このBOTでJPYN<:JPYNdisco:698471276498649168> をJPX<:jpxdis1:710400520434745425> にスワップ出来ます。\n【 /tip jpyn ●00 <@707133263562670140 】【 /tip jpyn ●00 @SWAP 】ただし、100JPYN × 整数倍数（1～10まで）のみになっています。\n例えば、[ /tip JPYN 200 <@707133263562670140> ]ならば0.0002JPX で自動交換されます。\nTipの小数点以下や、1JPYN～9JPYNはBOTは読み込みません。注意して下さい。\n不具合や不都合あれば、画面のスクリーンショットを撮り、それをもってDMやChatで報告して下さい。')  

    if now == '04:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('[@SWAP] You can swap JPYN<:JPYNdisco:698471276498649168>  to JPX<:jpxdis1:710400520434745425> with this BOT. \n[/ Tip jpyn ●00 <@ 707133263562670140】 [/ tip jpyn ●00 @SWAP】 However, only 100JPYN × integer multiples (1 to 10) are available.\n For example, [/ tip JPYN 200 <@ 707133263562670140>] will be replaced automatically at 0.0002JPX.\n BOT cannot be read below the decimal point of Tip or from 1JPYN to 9JPYN. be careful. \n If there is a problem or inconvenience, please take a screenshot of the screen and report it with DM or Chat.')

    if now == '07:19':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:jpxdis1:710400520434745425>✨')   

    if now == '10:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('［@SWAP］このBOTでJPYN<:JPYNdisco:698471276498649168> をJPX<:jpxdis1:710400520434745425> にスワップ出来ます。\n【 /tip jpyn ●00 <@707133263562670140 】【 /tip jpyn ●00 @SWAP 】ただし、100JPYN × 整数倍数（1～10まで）のみになっています。\n例えば、[ /tip JPYN 200 <@707133263562670140> ]ならば0.0002JPX で自動交換されます。\nTipの小数点以下や、1JPYN～9JPYNはBOTは読み込みません。注意して下さい。\n不具合や不都合あれば、画面のスクリーンショットを撮り、それをもってDMやChatで報告して下さい!👋')  

    if now == '10:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('[@SWAP] You can swap JPYN<:JPYNdisco:698471276498649168>  to JPX<:jpxdis1:710400520434745425> with this BOT. \n[/ Tip jpyn ●00 <@ 707133263562670140】 [/ tip jpyn ●00 @SWAP】 However, only 100JPYN × integer multiples (1 to 10) are available.\n For example, [/ tip JPYN 200 <@ 707133263562670140>] will be replaced automatically at 0.0002JPX.\n BOT cannot be read below the decimal point of Tip or from 1JPYN to 9JPYN. be careful. \n If there is a problem or inconvenience, please take a screenshot of the screen and report it with DM or Chat.') 


    if now == '10:55':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:jpxdis1:710400520434745425>👋')  

    if now == '14:12':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good01:699581068285706301> <:gn:699792795363311676>') 

    if now == '15:19':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:jpxdis1:710400520434745425>✨')   

    if now == '19:51':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:jpxdis1:710400520434745425>')  

    if now == '22:20':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:cafe:699769671234355230>Good morning<:jpxdis1:710400520434745425>') 

    if now == '21:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('$tip online 0.001 btt')
        
#ループ処理実行
loop.start()


@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "<a:jpynjpxani:710395215307079711> <a:jpynjpxani:710395215307079711> <a:jpynjpxani:710395215307079711>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:jpxdis1:710400520434745425> <:jpxdis1:710400520434745425> <:jpxdis1:710400520434745425>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:jpxdis1:710400520434745425>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:good:699580636448423936> <:jpxdis1:710400520434745425>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "三卍( ﾟ∀ﾟ)･∵. ｸﾞﾊｯ!!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"三卍( ﾟ∀ﾟ)･∵. ｸﾞﾊｯ!!")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "( ﾟдﾟ)ﾊｯ!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"( ﾟдﾟ)ﾊｯ!")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "((((-(-(-(-(-｡-)-)-)-)-))))":
        # チャンネルへメッセージを送信
        await message.channel.send(f"ｷｬ━━━━(ﾟ∀ﾟ)━━━━!!")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "ヾ(´∀｀)ﾉｷｬｯｷｬ":
        # チャンネルへメッセージを送信
        await message.channel.send(f"(((o(*ﾟ▽ﾟ*)o)))ワロタ")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "ヾ(*´∀｀*)ﾉ":
        # チャンネルへメッセージを送信
        await message.channel.send(f"(❁´ω`❁) ✧٩(ˊωˋ*)و✧")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "ありがとうございます":
        # チャンネルへメッセージを送信
        await message.channel.send(f"/tip bgpt 800000 {message.author.mention}さん ☆I am the one who should thank you☆")  # f文字列（フォーマット済み文字列リテラル）
        

    if message.content == "ありがとう！":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん　I am the one who should thank you～☆" )  # f文字列（フォーマット済み文字列リテラル）

        
    
    elif message.content == "r/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "r/language":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /language EN ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
              
    elif message.content == "r/accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

    elif message.content == "b/benzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
        
    elif message.content == "b/jpynzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記      
        
    elif message.content == "b/bgptzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info bgpt")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
    
    elif message.content == "b/kenjzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info kenj")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
             
    elif message.content == "b/sprtszan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info sprts")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 

    elif message.content == "b/29zan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info 29coin")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 

    elif message.content == "b/jpxzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/info jpx")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "b/gdrhzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info gdrh")
        [await q.add_reaction(i) for i in ('⭕',  '❌')]  # for文の内包表記
        
              
    elif message.content == "/tip jpyn 100 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0001 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 100 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0001 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 100 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0001 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ    

    elif message.content == "/tip JPYN 100 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0001 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        

    elif message.content == "/tip jpyn 200 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0002 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 200 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0002 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 200 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0002 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ    

    elif message.content == "/tip JPYN 200 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0002 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ


    elif message.content == "/tip jpyn 300 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0003 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 300 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0003 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 300 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0003 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ    

    elif message.content == "/tip JPYN 300 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0003 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 400 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0004 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 400 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0004 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 400 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0004 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ    

    elif message.content == "/tip JPYN 400 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0004 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ



    elif message.content == "/tip jpyn 500 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0005 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 500 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0005 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 500 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0005 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ    

    elif message.content == "/tip JPYN 500 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0005 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '😊',  '👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ


    elif message.content == "/tip jpyn 600 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0006 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 600 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0006 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 600 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0006 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip JPYN 600 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0006 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301> ', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        

    elif message.content == "/tip jpyn 700 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0007 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 700 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0007 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 700 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0007 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip JPYN 700 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0007 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301> ', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ



    elif message.content == "/tip jpyn 800 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0008 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 800 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0008 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 800 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0008 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip JPYN 800 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0008 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301> ', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ


    elif message.content == "/tip jpyn 900 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0009 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 900 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0009 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 900 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0009 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip JPYN 900 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.0009 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301> ', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ


    elif message.content == "/tip jpyn 1000 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.001 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '💗', '💜', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip jpyn 1000 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.001 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '💗', '💜', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ
        
    elif message.content == "/tip JPYN 1000 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.001 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '💗', '💜', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ

    elif message.content == "/tip JPYN 1000 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPX 0.001 {message.author.mention}  \n☞**_Swapped the <:JPYNdisco:698471276498649168> to <:jpxdis1:710400520434745425>_**\n\n:thumbsup::warning:\n:flag_gb:If you find it inconvenient, please take a screenshot and report it on DM or Chat.\n:flag_jp:もし不都合あればスクリーンショットを撮って、DMやChat等で報告して下さい。")
        [await q.add_reaction(i) for i in ('<:jpxdis1:710400520434745425>',  '<:good01:699581068285706301>', '💗', '💜', '😊','👌',  '👍', '😢',  '❌')]   # for文の内包表記とJPXのスワップ


 
        
    elif message.content == "/tip JPYN 10 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 10 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 10 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 10 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 10 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 10 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 10 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 10 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記


    elif message.content == "/tip JPYN 12.34 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 12.34 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 12.34 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 12.34 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 12.34 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 12.34 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 12.34 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 12.34 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記





    elif message.content == "/tip JPYN 20 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 20 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 20 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 20 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 20 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 20 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 20 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 20 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記


    elif message.content == "/tip JPYN 30 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 30 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 30 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 30 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 30 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 30 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 30 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 30 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記


    elif message.content == "/tip JPYN 40 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 40 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 40 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 40 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 40 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 40 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 40 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 40 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記


    elif message.content == "/tip JPYN 50 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 50 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 50 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 50 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 50 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 50 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 50 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 50 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記


    elif message.content == "/tip JPYN 60 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 60 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 60 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 60 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 60 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 60 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 60 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 60 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記



    elif message.content == "/tip JPYN 70 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 70 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 70 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 70 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 70 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 70 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 70 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 70 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記



    elif message.content == "/tip JPYN 80 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 80 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 80 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 80 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 80 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 80 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 80 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 80 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記



    elif message.content == "/tip JPYN 90 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 90 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 90 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 90 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 90 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 90 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 90 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 90 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記


    elif message.content == "/tip JPYN 99 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 99 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip JPYN 99 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 99 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 99 <@&711056506598064188>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 99 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記

    elif message.content == "/tip jpyn 99 <@707133263562670140>":
        # リアクションアイコンを付けたい
        q = await message.channel.send(f"/tip JPYN 99 {message.author.mention}  Return<:JPYNdisco:698471276498649168> ")
        [await q.add_reaction(i) for i in ('❌', '😢')]  # for文の内包表記



        
client.run(token)
