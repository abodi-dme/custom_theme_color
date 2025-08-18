/** Make the left logo/hamburger area navigate to the Odoo home (Apps) page. */
odoo.define('custom_theme_color.logo_click', function (require) {
    "use strict";

    const { onMounted } = owl;

    onMounted(() => {
        const goHome = () => { window.location.href = "/web"; };
        const toggle = document.querySelector('.o_main_navbar .o_menu_toggle');
        const brand  = document.querySelector('.o_main_navbar .o_menu_brand');

        if (toggle) toggle.addEventListener('click', goHome);
        if (brand)  brand.addEventListener('click', goHome);
    });
});
