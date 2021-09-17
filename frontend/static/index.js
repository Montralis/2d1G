const endpoints = {
    about: 'version',
    twoIdiots: 'two-idiots',
    guess: 'guess',
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
    },
    about: {
        data: '',
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
    const mode = data[modeName];
    const endpoint = `/${endpoints[modeName]}`;

    try {
        console.log(`Trying to fetch "${endpoint}"...`);
        const res = await fetch(endpoint);
        const json = await res.json();

        if (json.error) {
            handleError(json.error);
        } else {
            mode.data = json;
        }
    } catch (err) {
        console.error(err);
        data.error = err;
    }
}

function handleError(error) {
    console.error(error);
    data.error = error;
}

function incIndex() {
    const mode = data[data.modeName];
    mode.index = mode.index < mode.data.length - 1 ? mode.index + 1 : 0;
}
