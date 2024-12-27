require('dotenv').config(); // dotenv 설정

const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages],
});
const axios = require('axios');
const {checkNewPost, getBotMessage} = require('./src/controller/apiController');
const logger = require('./src/utils/logger');

const token = process.env.BOT_TOKEN; // .env에서 봇 토큰 가져오기
const targetChannelId = process.env.CHANNEL_ID; // 메시지를 보낼 채널의 ID
const messageInterval = 3600000; // 메시지 간격 (밀리초 단위), 여기선 1시간

client.once('ready', () => {
    //console.log(`${client.user.tag} 봇이 온라인 상태입니다!`);
    logger.info(`${client.user.tag} bot is online.`);
    // 특정 시간마다 메시지 보내기
    setInterval(() => {
        if (checkNewPost()) {
            const channel = client.channels.cache.get(targetChannelId);
            if (channel) {
                const message = getBotMessage();
                channel.send(message);
            } else {
                logger.error('Channel ID not found.');
            }
        } else {
            logger.info('Checked update, found none');
        }
    }, messageInterval);
});

client.on('messageCreate', (message) => {
    if (message.content === 'ping') {
        message.reply('pong!');
    }
});

client.login(token);
