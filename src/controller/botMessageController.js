const generateBotMessage = (data) => {
    const response = `
    **공모 게시글 정보**
- **글번호**: ${data.post_number}
- **글제목**: ${data.post_title}
- **링크**: [바로가기](${data.post_url})
- **게시일**: ${data.post_date}
- **신청일**: ${data.application_date}
    `.trim();
    return response;
}

module.exports = {generateBotMessage}