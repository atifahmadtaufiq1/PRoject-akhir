import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!! bot is ready, I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def polusi(ctx):
    # kode untuk bot menerima gambar
    if ctx.message.attachments: 
        for file in ctx.message.attachments: 
            file_name = file.filename 
            file_url = file.url
            await file.save(f'./{file.filename}')
            hasil = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path=f'./{file.filename}')
            
            # kode untuk memproses gambar (ubah dengan melihat labels.txt)
            if hasil[0] == 'polusi udara\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah polusi udara')
                await ctx.send('polusi udara adalah kondisi di mana udara tercemar oleh zat-zat berbahaya yang dapat membahayakan kesehatan manusia, makhluk hidup lainnya, serta lingkungan.')
                await ctx.send('polusi udara di sebabkan emisi kendaraan bermotor,pabrik,kebakaran hutan,bahan kimia')
            elif hasil[0] == 'polusi tanah\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah polusi tanah')
                await ctx.send('Polusi tanah adalah kondisi di mana tanah tercemar oleh bahan-bahan berbahaya yang dapat merusak kualitas tanah, mengganggu kesehatan ekosistem, dan membahayakan organisme yang hidup di dalamnya, termasuk manusia')
                await ctx.send('Polusi tanah sering disebabkan oleh aktivitas manusia, seperti pembuangan limbah industri, limbah rumah tangga, penggunaan pestisida dan pupuk kimia secara berlebihan, serta penimbunan sampah yang tidak dikelola dengan baik')
            elif hasil[0] == 'polusi air\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah polusi air')
                await ctx.send('polusi air adalah kondisi di mana air, baik itu di sungai, danau, laut, atau sumber daya air lainnya, tercemar oleh zat-zat berbahaya yang dapat merusak ekosistem dan mengancam kesehatan manusia serta makhluk hidup lainnya')
                await ctx.send('penyebab utama polusi air adalah pembuangan limbah industri, rumah tangga, dan pertanian secara tidak tepat, penggunaan pestisida dan pupuk kimia yang berlebihan, serta tumpahan minyak atau bahan kimia berbahaya')
            else:
                await ctx.send('GAMBAR MU KEMUNGKINAN: salah format/blur/corrupt')
                await ctx.send('KIRIM GAMBAR BARU!!!')
    else:
        await ctx.send('GAMBAR TIDAK VALID/GAADA >:/')
