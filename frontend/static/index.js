const config = {
    endpoints: {
        about: 'version',
        twoIdiots: 'two-idiots',
        guess: 'guess',
    },
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
    const url = `/${config.endpoints[modeName]}`;
    const mode = data[modeName];

    try {
        const res = await fetch(url);
        mode.data = await res.json();
    } catch (err) {
        console.error(err);
        data.error = err;
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
