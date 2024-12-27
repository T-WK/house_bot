const generateBotMessage = (data) => {
    const response = '';
    response = `
    **공모 게시글 정보**
- **글번호**: ${data.글번호}
- **글제목**: ${data.글제목}
- **링크**: [바로가기](${data.글링크})
- **게시일**: ${data.게시일}
- **신청일**: ${data.신청일}
    `.trim();
    return response;
}

module.exports = {generateBotMessage}