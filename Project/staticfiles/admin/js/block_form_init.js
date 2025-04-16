document.addEventListener('DOMContentLoaded', function () {
    // Находим все inline-related блоки
    const blocks = document.querySelectorAll('.inline-related');
    if (blocks.length === 0) {
        return;
    }

    blocks.forEach(function (block) {
        // Находим выпадающий список типа блока
        const typeSelect = block.querySelector('select[name$="-type"]');
        if (typeSelect) {
            // Функция для обновления видимости полей
            const updateFieldVisibility = function () {
                // Сначала скрываем все поля с data-field-type
                block.querySelectorAll('[data-field-type]').forEach(function (field) {
                    const formRow = field.closest('.form-row');
                    formRow.style.display = 'none';
                });

                // Показываем только нужное поле в зависимости от выбранного типа
                const selectedType = typeSelect.value;
                if (selectedType) {
                    const targetField = block.querySelector(`[data-field-type="${selectedType}"]`);
                    if (targetField) {
                        const formRow = targetField.closest('.form-row');
                        formRow.style.display = '';
                    }
                }
            };

            // Вызываем функцию при загрузке страницы
            updateFieldVisibility();

            // Добавляем обработчик onchange для будущих изменений
            typeSelect.onchange = updateFieldVisibility;
        }
    });
});