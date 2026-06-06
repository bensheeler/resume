import unittest

from build_resume import render_experience, render_header, render_projects


class RenderExperienceTests(unittest.TestCase):
    def test_repeats_company_for_each_role(self):
        experience = [
            {
                "company": "Example Corp",
                "location": "Remote",
                "roles": [
                    {
                        "title": "Senior Software Engineer",
                        "start": "March 2022",
                        "end": "current",
                        "highlights": ["Led service migration."],
                    },
                    {
                        "title": "Software Engineer",
                        "start": "January 2020",
                        "end": "March 2022",
                        "highlights": ["Built backend services."],
                    },
                ],
            }
        ]

        typst = render_experience(experience)

        self.assertEqual(typst.count('[*Example Corp* -'), 2)
        self.assertIn('[*Example Corp* - Senior Software Engineer]', typst)
        self.assertIn('[*Example Corp* - Software Engineer]', typst)
        self.assertIn('[March 2022 - Present]', typst)
        self.assertIn('[Remote]', typst)
        self.assertIn('- Led service migration.', typst)
        self.assertIn('- Built backend services.', typst)
        self.assertIn('#v(0.35em)', typst)

    def test_uses_georgia_font(self):
        typst = render_header({"name": "Test Person"})

        self.assertIn('font: "Georgia"', typst)

    def test_renders_projects_when_present(self):
        projects = [
            {
                "name": "Resume Builder",
                "link": "https://github.com/example/resume",
                "summary": "Generate a Typst resume from structured YAML data.",
                "highlights": ["Rendered resume sections from YAML into Typst."],
                "tech": ["Python", "YAML", "Typst"],
            }
        ]

        typst = render_projects(projects)

        self.assertIn("== Projects", typst)
        self.assertIn("*Resume Builder*", typst)
        self.assertIn("https://github.com/example/resume", typst)
        self.assertIn("Generate a Typst resume from structured YAML data.", typst)
        self.assertIn("- Rendered resume sections from YAML into Typst.", typst)
        self.assertIn("- *Key Tech* - Python, YAML, Typst", typst)


if __name__ == "__main__":
    unittest.main()
