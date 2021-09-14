const config = {
    backendUrl: 'http://localhost:5000',
    endpoints: {
        twoIdiots: 'randomTwoIdiots',
        guess: 'randomGuess',
    },
};

let data = {
    modeName: 'home',
    titles: {
        home: 'Wähle ein Trinkspiel aus',
        twoIdiots: '2 Dumme 1 Gedanke',
        guess: 'Schätzfragen',
    },
    twoIdiots: {
        index: 0,
        data: [],
    },
    guess: {
        index: 0,
        answerVisible: false,
        data: [],
    },
};

document.addEventListener('alpine:init', () => {
    console.log(`Loaded Alpine.js v${Alpine.version}`);
    data = Alpine.reactive(data);
});

async function loadData() {
    const modeName = data.modeName;
    const url = `${config.backendUrl}/${config.endpoints[modeName]}`;
    const mode = data[modeName];

    try {
        const res = await fetch(url);
        mode.data = await res.json();
    } catch (err) {
        console.error(err);
    }
}

function incIndex() {
    const mode = data[data.modeName];

    if (mode.index < mode.data.length - 1) {
        mode.index++;
    } else {
        mode.index = 0;
    }
}
