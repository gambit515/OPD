document.addEventListener('DOMContentLoaded', function () {
    const typeField = document.getElementById('id_type');
    const descriptionField = document.getElementById('id_description');
    const imageField = document.getElementById('id_image');
    const videoUrlField = document.getElementById('id_video_url');
    const listItemsField = document.getElementById('id_list_items');

    function toggleFields() {
        // Скрываем все поля
        descriptionField.closest('.form-row').style.display = 'none';
        imageField.closest('.form-row').style.display = 'none';
        videoUrlField.closest('.form-row').style.display = 'none';
        listItemsField.closest('.form-row').style.display = 'none';

        // Показываем только нужные поля
        if (typeField.value === 'text') {
            descriptionField.closest('.form-row').style.display = '';
        } else if (typeField.value === 'image') {
            imageField.closest('.form-row').style.display = '';
        } else if (typeField.value === 'video') {
            videoUrlField.closest('.form-row').style.display = '';
        } else if (typeField.value === 'list') {
            listItemsField.closest('.form-row').style.display = '';
        }
    }

    // Инициализация при загрузке страницы
    toggleFields();

    // Обновление полей при изменении типа блока
    typeField.addEventListener('change', toggleFields);
});