require('dotenv').config();
const { generateBotMessage } = require('./botMessageController');
const axios = require('axios');
const logger = require('../utils/logger');

const baseUrl = process.env.CRAWLER_URL; 
const checkApiPath = "/api/posts/new-counts"
const getDataPath = "/api/posts/recent-posts"

const checkNewPost = async () => {
    const url = `${baseUrl}${checkApiPath}`
    try {
        const response = await axios.get(url); // API에 GET 요청
        if (response.data.status === "error") {
            logger.error('Error in crawler:', response.data.message);
            return -1;
        }
        return response.data.data;
    } catch (error) {
        logger.error('Error while processing Interval', error.message);
        return false;
    }
}

const getBotMessage = async (cnt) => {
    const url = `${baseUrl}${getDataPath}`
    try {
        const response = await axios.get(url,{params: {count:cnt}});
        if (response.data.status === "error") {
            logger.error('crawler responsed "error":', response.data.message);
            return '!!크롤링 서버 오류!!'
        }
        const posts = response.data.data;
        if (!Array.isArray(posts) || posts.length === 0) {
            logger.info('No posts found in the API response.');
            return '!!게시글이 없습니다!!';
        }
        const messages = posts.map(post => { return generateBotMessage(post) });
        const res = messages.join('\n\n');
        return "📌 **공모 게시글 정보**\n\n"+res;

    } catch (error){
        logger.error('Something went wrong while generating bot message', {
            message: error.message,
            stack: error.stack,
            ...(error.response && { status: error.response.status, data: error.response.data })
        });
        return '!!API 요청 오류!!'
    }
}
module.exports = {checkNewPost, getBotMessage}