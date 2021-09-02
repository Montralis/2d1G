const config = {
    backendUrl: 'http://localhost:5000',
};

const data = {
    mode: 'home',
    twoIdiots: {
        categorie: '',
    },
    guess: {
        frage: '',
        antwort: '',
        answerVisible: false,
    },
};

async function fetchResult(endpoint) {
    const url = `${config.backendUrl}/${endpoint}`;

    try {
        const res = await fetch(url);
        const json = await res.json();
        return json.result;
    } catch (err) {
        console.error(err);
    }
}

async function getRandCategory() {
    return fetchResult('randomTwo');
}

async function getRandSchaetzfrage() {
    return fetchResult('randomSchaetzen');
}
