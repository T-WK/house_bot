require('dotenv').config();
const { generateBotMessage } = require('./botMessageController');
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
        logger.error('Error while processing Interval', error.message);
        return false;
    }
}

const getBotMessage = async () => {
    const url = `${baseUrl}${getDataPath}`
    try {
        const response = await axios.get(url);
        if (response.data.status === "error") {
            logger.error('crawler responsed "error":', response.data.message);
            return '!!크롤링 서버 오류!!'
        }
        const data = await JSON.parse(JSON.stringify(response.data.data));
        const parsedData = JSON.parse(data);
        logger.info(parsedData);
        const res = await generateBotMessage(parsedData);
        return res;

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