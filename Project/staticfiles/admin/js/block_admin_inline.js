(function($) {
    function toggleFields() {
        // Сначала скрываем все специфичные поля
        $('#id_blocks-TOTAL_FORMS').closest('fieldset.module').find('.field-description, .field-image, .field-video_url, .field-list_items').hide();

        // Проходим по всем блокам
        $('.dynamic-blocks').each(function() {
            var prefix = $(this).attr('id').replace('-empty', '').replace('blocks-', '');
            var typeSelect = $('#id_blocks-' + prefix + '-type');

            if (typeSelect.length) {
                var selectedType = typeSelect.val();

                // Показываем только нужные поля в зависимости от выбранного типа
                if (selectedType === 'text') {
                    $('#id_blocks-' + prefix + '-description').closest('.form-row').show();
                } else if (selectedType === 'image') {
                    $('#id_blocks-' + prefix + '-image').closest('.form-row').show();
                } else if (selectedType === 'video') {
                    $('#id_blocks-' + prefix + '-video_url').closest('.form-row').show();
                } else if (selectedType === 'list') {
                    $('#id_blocks-' + prefix + '-list_items').closest('.form-row').show();
                }
            }
        });
    }

    $(document).ready(function() {
        // Инициализация при загрузке страницы
        toggleFields();

        // Обработчик изменения типа блока
        $('#id_blocks-TOTAL_FORMS').closest('fieldset.module').on('change', '.field-type select', function() {
            var prefix = $(this).closest('.inline-related').attr('id').replace('blocks-', '');
            // Сначала скрываем все специфичные поля для этого блока
            $('#id_blocks-' + prefix + '-description').closest('.form-row').hide();
            $('#id_blocks-' + prefix + '-image').closest('.form-row').hide();
            $('#id_blocks-' + prefix + '-video_url').closest('.form-row').hide();
            $('#id_blocks-' + prefix + '-list_items').closest('.form-row').hide();

            // Показываем только нужное поле
            if ($(this).val() === 'text') {
                $('#id_blocks-' + prefix + '-description').closest('.form-row').show();
            } else if ($(this).val() === 'image') {
                $('#id_blocks-' + prefix + '-image').closest('.form-row').show();
            } else if ($(this).val() === 'video') {
                $('#id_blocks-' + prefix + '-video_url').closest('.form-row').show();
            } else if ($(this).val() === 'list') {
                $('#id_blocks-' + prefix + '-list_items').closest('.form-row').show();
            }
        });

        // Обработка добавления новых блоков
        $('#blocks-group .add-row a').on('click', function() {
            setTimeout(toggleFields, 100); // Даем время для рендеринга нового блока
        });
    });
})(django.jQuery);