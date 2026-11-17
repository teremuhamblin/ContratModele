from pathlib import Path
import re
import sys
import unittest

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))

import generate  # noqa: E402


class TestContratModele(unittest.TestCase):

    def test_all_templates_have_valid_placeholders_and_warning(self):
        templates = generate.list_templates()
        self.assertGreaterEqual(len(templates), 5)
        for tpl in templates:
            text = tpl.read_text(encoding="utf-8")
            self.assertIn("Avertissement", text, f"Avertissement manquant dans {tpl.name}")
            self.assertNotIn("XXXX", text, f"Marqueur XXXX résiduel dans {tpl.name}")
            placeholders = generate.extract_placeholders(text)
            self.assertGreater(len(placeholders), 0, f"Aucune variable {{{{...}}}} dans {tpl.name}")
            for key in placeholders:
                self.assertRegex(key, r"^[A-Z0-9_]+$")

    def test_strip_pedagogical_blocks(self):
        sample = (
            "> ⚠️ **Avertissement :** Info.\n\n"
            "> **Instructions d'utilisation :**\n> - Ligne 2\n\n---\n\n"
            "# Contrat Test\n\n"
            "> 💡 **Explication**\n> Blabla\n\n"
            "## Article 1\nContenu {{CLIENT_RAISON_SOCIALE}}.\n"
        )
        cleaned = generate.strip_pedagogical_blocks(sample)
        self.assertNotIn("Avertissement", cleaned)
        self.assertNotIn("Instructions d'utilisation", cleaned)
        self.assertNotIn("Explication", cleaned)
        self.assertIn("# Contrat Test", cleaned)
        self.assertIn("Contenu {{CLIENT_RAISON_SOCIALE}}.", cleaned)

    def test_render_template_replaces_variables(self):
        tpl = "> ⚠️ **Avertissement :** Test\n\n# Contrat\nClient : {{CLIENT_RAISON_SOCIALE}}\n"
        rendered = generate.render_template(tpl, {"CLIENT_RAISON_SOCIALE": "ACME SAS"})
        self.assertEqual(rendered, "# Contrat\nClient : ACME SAS\n")

    def test_siret_and_lme_validation(self):
        self.assertEqual(generate.validate_field("CLIENT_SIRET", "73282932000074"), [])
        self.assertTrue(len(generate.validate_field("CLIENT_SIRET", "12345")) > 0)
        self.assertEqual(generate.validate_field("DELAI_PAIEMENT_JOURS", "30"), [])
        self.assertTrue(len(generate.validate_field("DELAI_PAIEMENT_JOURS", "90")) > 0)

    def test_sanitize_filename_blocks_traversal(self):
        self.assertEqual(generate.sanitize_filename("../../etc/passwd", "fallback"), "fallback")
        self.assertEqual(generate.sanitize_filename("mon-contrat.md", "fallback"), "mon-contrat")


if __name__ == "__main__":
    unittest.main()
