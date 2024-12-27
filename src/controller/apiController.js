require('dotenv').config();
const generateBotMessage = require('./botMessageController');
const axios = require('axios');
const logger = require('../utils/logger');

const baseUrl = process.env.CRAWLER_URL; 
const checkApiPath = "/api/posts/check-new"
const getDataPath = "/api/posts/recent-post"

const checkNewPost = async () => {
    const url = `${baseUrl}${checkApiPath}`
    try {
        const response = await axios.get(url); // API에 GET 요청
        if (response.data.status === "error") {
            logger.error('Error in crawler:', response.data.message);
            return false;
        }
        return response.data.data === true; // 반환 값이 true인지 확인
    } catch (error) {
        logger.error('Error while processing Interval');
        return false;
    }
}

const getBotMessage = async () => {
    const url = `${baseUrl}${getDataPath}`
    const postData = ''
    try {
        const response = await axios.get(url);
        if (response.data.status === "error") {
            logger.error('crawler responsed "error":', response.data.message);
            postData = '!!크롤링 서버 오류!!'
            return postData
        }
        return generateBotMessage(response.data.data);

    } catch {
        logger.error('something went wrong while generating bot message');
        postData = '!!API 요청 오류!!'
        return postData
    }
}
module.exports = {checkNewPost, getBotMessage}