import pathlib

import pylexibank
from idspy import IDSDataset, IDSEntry


class Dataset(IDSDataset):
    dir = pathlib.Path(__file__).parent
    id = "yuchinese"
    writer_options = dict(keep_languages=False, keep_parameters=False)

    form_spec = pylexibank.FormSpec(
        normalize_unicode="NFD",
        replacements=[(" ", "_"), ("...", ""), ("’", "_"), ("'", "_")],
    )

    def cldf_specs(self):
        return super().cldf_specs()

    def cmd_download(self, args):
        self.raw_dir.xlsx2csv("ids_cl_chinese(mandarin).xlsx")

    def cmd_makecldf(self, args):
        glottocode = "mand1415"
        reprs = ["Pinyin", "StandOrth (Simplified)", "StandOrth (Traditional)"]

        args.writer.add_concepts(id_factory=lambda c: c.attributes["ids_id"])
        args.writer.add_sources(*self.raw_dir.read_bib())

        personnel = self.get_personnel(args)

        args.writer.add_language(
            ID=glottocode,
            Name="Mandarin Chinese",
            Glottocode=glottocode,
            Authors=personnel["author"],
            DataEntry=personnel["data entry"],
            Consultants=personnel["consultant"],
            Representations=reprs,
            date="2021-02-24",
        )

        for form in pylexibank.progressbar(self.read_csv("ids_cl_chinese(mandarin).Sheet1.csv")):
            if form.form:
                args.writer.add_lexemes(
                    Language_ID=glottocode,
                    Parameter_ID=form.ids_id,
                    Value=form.form,
                    Comment=form.comment,
                    Source="yuhsiaojung2021",
                    Transcriptions=reprs,
                    AlternativeValues=form.alt_forms,
                )

        self.apply_cldf_defaults(args)

    def entry_from_row(self, row):
        return IDSEntry("{0}-{1}".format(row[0], row[1]), row[3], [row[4], row[5]], row[6])
