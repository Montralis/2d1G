const config = {
    backendUrl: 'http://localhost:5000',
};

const data = {
    mode: 'home',
    titles: {
        home: 'Wähle ein Trinkspiel aus',
        twoIdiots: '2 Dumme 1 Gedanke',
        guess: 'Schätzfragen',
    },
    twoIdiots: {
        categorie: null,
    },
    guess: {
        frage: null,
        antwort: null,
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
    const result = await fetchResult('randomTwo');
    return result ? result : { categorie: null };
}

async function getRandSchaetzfrage() {
    const result = await fetchResult('randomSchaetzen');
    return result ? result : {
        frage: null,
        antwort: null,
        answerVisible: false,
    };
}
