from django.test.utils import tag

from tests import models, test_case


@tag("functional", "functional_widget", "widget")
class RequiredWidgetStackedInlineTestCase(test_case.IUWTestCase):
    model = "testrequiredinline"

    def test_build_new_widget(self):
        self.assertEqual(models.TestRequiredInlineItem.objects.count(), 0)

        self.goto_add_page()
        inlines = self.page.query_selector_all(".inline-related:not(.empty-form)")
        self.assertEqual(len(inlines), 0)

        add_row = self.page.query_selector(".add-row a")
        add_row.click()
        add_row.click()

        inlines = self.page.query_selector_all(".inline-related:not(.empty-form)")
        self.assertEqual(len(inlines), 2)

        for inline in inlines:
            iuw = inline.query_selector(".iuw-root")
            file_input = iuw.query_selector("input[type=file]")

            self.assertIsNotNone(iuw)
            self.assertIsNotNone(file_input)

            file_input.set_input_files(self.image1)

            preview = self.find_widget_preview(iuw)
            img = preview.query_selector("img")
            preview_button = self.find_preview_icon(preview)
            self.assertTrue(preview.is_visible())
            self.assertIsNotNone(img)
            self.assertIsNotNone(preview_button)

        self.submit_form("#testrequiredinline_form")

        itens = models.TestRequiredInlineItem.objects.all()
        self.assertEqual(len(itens), 2)
        for item in itens:
            self.assertIsNotNone(item.image)
