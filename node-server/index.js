require('dotenv').config(); // dotenv 설정

const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});
const {checkNewPost, getBotMessage} = require('./src/controller/apiController');
const logger = require('./src/utils/logger');

const token = process.env.BOT_TOKEN; // .env에서 봇 토큰 가져오기
const targetChannelId = process.env.CHANNEL_ID; // 메시지를 보낼 채널의 ID
const messageInterval = 3600000; // 메시지 간격 (밀리초 단위), 여기선 1시간

client.once('ready', () => {
    //console.log(`${client.user.tag} 봇이 온라인 상태입니다!`);
    logger.info(`${client.user.tag} bot is online.`);
    handlePostUpdates();
    // 특정 시간마다 메시지 보내기
    setInterval(handlePostUpdates, messageInterval);
});

//feature test
client.on('messageCreate', async (message) => {
    if (message.content === 'ping') {
        message.reply('pong!');
    } else if (message.content === '집' || message.content === 'h') {
        handlePostUpdates();
    }
});

client.login(token);

const handlePostUpdates = async () => {
    const post_cnt = await checkNewPost();
    if (post_cnt > 0) {
        const channel = client.channels.cache.get(targetChannelId);
        const message = await getBotMessage(post_cnt);
        channel.send(message);
    } else {
        logger.info('Checked update, found none');
    }
}