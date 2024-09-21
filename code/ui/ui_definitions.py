from ui.uicore.ui_canvas import *
from settings import *
from ui.ui_button import UI_Button
from ui.ui_text import UI_Text

UI_NEXT_BUTTON = UIDefinitionData(
    UI_Canvas,
    (WINDOW_WIDTH - 220, WINDOW_HEIGHT - 120),
    (200, 100),
    (100, 50),
    (20, 20),
    (100, 100, 100),
    255,
    EStackingMode.VERTICAL,
    [UIDefinitionData(
        UI_Button,
        (WINDOW_WIDTH - 220, WINDOW_HEIGHT - 120),
        (200, 100),
        (100, 50),
        (20, 20),
        (175, 175, 175),
        255,
    EStackingMode.VERTICAL,
    [UIDefinitionData(UI_Text)])
    ])
