require("dotenv").config({ path: "./assets/modules/.env" });
const TelegramBot = require('node-telegram-bot-api')
const bot = new TelegramBot(process.env.devStatus ? process.env.tokenTest : process.env.tokenDefault, {polling: true})
const keyboard = require("./assets/keyboard/keyboard")
const { first } = require('./assets/logic/logic')
const fs = require('fs')
const accounts = require('./assets/db/accounts.json');

bot.on('message', async msg => {
    if (msg.text === '/start'){
        await bot.sendMessage(msg.chat.id, "hello world", keyboard)
    }
    if (msg.text === 'Добавить инстаграм канал'){
        let account = JSON.parse(fs.readFileSync('./assets/db/accounts.json'))
        await bot.sendMessage(msg.chat.id, "пришли канал")
        if (!account){
            accounts.push({
                account: msg.text
            })
            fs.writeFileSync('./assets/db/accounts.json', JSON.stringify(accounts, null, '\t'))
            console.log('аккаунт добвлен')
        }
    }

    if (msg.text === 'cпарсить инстаграм'){
        await bot.sendMessage(msg.chat.id, "инстаграм начал парсится")
        first()
    }

    if (msg.text === 'запостить в телеграм канал'){
        console.log(msg)
        if (msg.chat.id === '1425448286'){
            try{
                await bot.sendMessage(process.env.channelId, `${require("").default}`) 
                await bot.sendMessage(msg.chat.id, "пост был отправлен")
            }catch(error){
                console.log(`error in posting to telegram channel appeared error: ${error}`)
            }
        }
    }
})
bot.on('polling_error', console.log)