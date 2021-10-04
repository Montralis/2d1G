const repository = 'https://github.com/Montralis/2d1G';

const endpoints = {
    twoIdiots: 'two-idiots',
    guess: 'guess',
    differentWord: 'different-word',
};

let data = {
    error: null,
    modeName: 'home',
    titles: {
        home: 'Wähle ein Trinkspiel aus',
        about: 'Über diese Seite',
        addData: 'Neue Daten hinzufügen',
        twoIdiots: '2 Dumme 1 Gedanke',
        guess: 'Schätzfragen',
        differentWord: 'Anderes Wort für...',
    },
    about: {
        flaskVersion: '',
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
    differentWord: {
        index: 0,
        data: [],
    },
    repository,
};

document.addEventListener('alpine:init', () => {
    console.log(`Loaded Alpine.js v${Alpine.version}`);
    data = Alpine.reactive(data);
});

function handleError(error) {
    console.error(error);
    data.error = error;
}

async function loadData(endpoint) {
    try {
        console.log(`Trying to fetch "${endpoint}"...`);
        const res = await fetch(endpoint);
        const json = await res.json();

        if (json.error) {
            handleError(json.error);
        } else {
            return json;
        }
    } catch (error) {
        handleError(error);
    }
}

async function loadGameData() {
    const modeName = data.modeName;
    const mode = data[modeName];
    const endpoint = `/game/${endpoints[modeName]}`;

    mode.data = await loadData(endpoint);
}

function incIndex() {
    const mode = data[data.modeName];
    mode.index = mode.index < mode.data.length - 1 ? mode.index + 1 : 0;
}
