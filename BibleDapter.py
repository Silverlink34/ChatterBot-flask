from chatterbot.logic import LogicAdapter
import pythonbible as bible


class BibleDapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        refsWereFound = False
        matchedRefs = bible.get_references(statement.text)
        if matchedRefs:
            refsWereFound = True
        return refsWereFound

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        matchedRefs = bible.get_references(input_statement.text)
        verseIds = bible.convert_references_to_verse_ids(matchedRefs)
        allVersesList = [bible.get_verse_text(verseId) for verseId in verseIds]
        allVersesString = '\n'.join(allVersesList)
        bible_response = Statement(text=allVersesString)
        confidence = 1
        return confidence, bible_response