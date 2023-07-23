;(function() {
    const modal = new bootstrap.Modal(document.getElementById('formModal'));

    htmx.on('htmx:afterSwap', (e) => {
        if (e.detail.target.id === 'modalDialog') {
            modal.show();
        }
    });

    htmx.on('htmx:beforeSwap', (e) => {
        if (e.detail.target.id === 'modalDialog' && !e.detail.xhr.response) {
            modal.hide();
            e.detail.shouldSwap = false;
        }
    });

    htmx.on('hidden.bs.modal', (e) => {
        document.getElementById('modalDialog').innerHTML = '';
    });
})();