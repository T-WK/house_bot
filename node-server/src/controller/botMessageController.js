const generateBotMessage = (data) => {
    const response = `
**${data.post_number}**: ${data.post_title}
**게시일**: ${data.post_date}
**신청일**: ${data.application_date}
**링크**: <${data.post_url}>
    \n`.trim();
    return response;
}

module.exports = {generateBotMessage}