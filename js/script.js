$(document).ready(function () {
    $('select').formSelect();
    $('input.autocomplete').autocomplete({
        data: {
            "Brasília": null,
            "Ceilândia": null,
            "Estrutural": null,
            "Gama": null,
            "Planaltina": null,
            "Recanto das Emas": null,
            "Riacho Fundo": null,
            "Samambaia": null,
            "São Sebastião": null,
            "Taguatinga": null,
        },
    });
});