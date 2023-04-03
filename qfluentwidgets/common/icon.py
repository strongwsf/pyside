# coding:utf-8
from enum import Enum

from qtpy.QtXml import QDomDocument
from qtpy.QtCore import QPoint, QRect, QRectF, Qt, QFile
from qtpy.QtGui import QIcon, QIconEngine, QImage, QPainter, QPixmap, QColor
from qtpy.QtSvg import QSvgRenderer

from .config import isDarkTheme, Theme


class IconEngine(QIconEngine):
    """ Icon engine """

    def __init__(self, iconPath):
        self.iconPath = iconPath
        super().__init__()

    def paint(self, painter, rect, mode, state):
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.SmoothPixmapTransform)
        if not self.iconPath.lower().endswith('svg'):
            painter.drawImage(rect, QImage(self.iconPath))
        else:
            drawSvgIcon(self.iconPath, painter, rect)

    def pixmap(self, size, mode, state):
        pixmap = QPixmap(size)
        pixmap.fill(Qt.transparent)
        self.paint(QPainter(pixmap), QRect(QPoint(0, 0), size), mode, state)
        return pixmap


class Icon(QIcon):

    def __init__(self, iconPath):
        self.iconPath = iconPath
        super().__init__(IconEngine(iconPath))


class MenuIconEngine(QIconEngine):

    def __init__(self, icon):
        super().__init__()
        self.icon = icon

    def paint(self, painter, rect, mode, state):
        self.icon.paint(painter, rect, Qt.AlignHCenter, QIcon.Normal, state)


def getIconColor():
    """ get the color of icon based on theme """
    return "white" if isDarkTheme() else 'black'


def drawSvgIcon(icon, painter, rect):
    """ draw svg icon

    Parameters
    ----------
    icon: str | bytes | QByteArray
        the path or code of svg icon

    painter: QPainter
        painter

    rect: QRect | QRectF
        the rect to render icon
    """
    renderer = QSvgRenderer(icon)
    renderer.render(painter, QRectF(rect))


def writeSvg(iconPath: str, indexes=None, **attributes):
    """ write svg with specified attributes

    Parameters
    ----------
    iconPath: str
        svg icon path

    indexes: List[int]
        the path to be filled

    **attributes:
        the attributes of path

    Returns
    -------
    svg: str
        svg code
    """
    if not iconPath.lower().endswith('.svg'):
        return ""

    f = QFile(iconPath)
    f.open(QFile.ReadOnly)

    dom = QDomDocument()
    dom.setContent(f.readAll())

    f.close()

    # change the color of each path
    pathNodes = dom.elementsByTagName('path')
    indexes = range(pathNodes.length()) if not indexes else indexes
    for i in indexes:
        element = pathNodes.at(i).toElement()

        for k, v in attributes.items():
            element.setAttribute(k, v)

    return dom.toString()


def drawIcon(icon, painter, rect):
    """ draw icon

    Parameters
    ----------
    icon: str | QIcon | FluentIconBaseBase
        the icon to be drawn

    painter: QPainter
        painter

    rect: QRect | QRectF
        the rect to render icon
    """
    if isinstance(icon, FluentIconBase):
        icon.render(painter, rect)
    else:
        icon = QIcon(icon)
        rect = QRectF(rect).toRect()
        image = icon.pixmap(rect.width(), rect.height())
        painter.drawPixmap(rect, image)


class FluentIconBase:
    """ Fluent icon base class """

    def path(self, theme=Theme.AUTO):
        """ get the path of icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`
        """
        raise NotImplementedError

    def icon(self, theme=Theme.AUTO):
        """ create an fluent icon

        Parameters
        ----------
        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`
        """
        return QIcon(self.path(theme))

    def render(self, painter, rect, theme=Theme.AUTO):
        """ draw svg icon

        Parameters
        ----------
        painter: QPainter
            painter

        rect: QRect | QRectF
            the rect to render icon

        theme: Theme
            the theme of icon
            * `Theme.Light`: black icon
            * `Theme.DARK`: white icon
            * `Theme.AUTO`: icon color depends on `config.theme`
        """
        drawSvgIcon(self.path(theme), painter, rect)


class FluentIcon(FluentIconBase, Enum):
    """ Fluent icon """

    ADD = "Add"
    CUT = "Cut"
    PIN = "Pin"
    TAG = "Tag"
    WEB = "Web"
    CHAT = "Chat"
    COPY = "Copy"
    CODE = "Code"
    EDIT = "Edit"
    FONT = "Font"
    HELP = "Help"
    HOME = "Home"
    INFO = "Info"
    LINK = "Link"
    MAIL = "Mail"
    MENU = "Menu"
    MORE = "More"
    SEND = "Send"
    SYNC = "Sync"
    ZOOM = "Zoom"
    ALBUM = "Album"
    BRUSH = "Brush"
    CLOSE = "Close"
    EMBED = "Embed"
    HEART = "Heart"
    MOVIE = "Movie"
    MUSIC = "Music"
    PHOTO = "Photo"
    PHONE = "Phone"
    VIDEO = "Video"
    PASTE = "Paste"
    CAMERA = "Camera"
    CANCEL = "Cancel"
    FOLDER = "Folder"
    SCROLL = "Scroll"
    LAYOUT = "Layout"
    GITHUB = "GitHub"
    SEARCH = "Search"
    UPDATE = "Update"
    RETURN = "Return"
    ZOOM_IN = "ZoomIn"
    SETTING = "Setting"
    PALETTE = "Palette"
    MESSAGE = "Message"
    ZOOM_OUT = "ZoomOut"
    FEEDBACK = "Feedback"
    MINIMIZE = "Minimize"
    CHECKBOX = "CheckBox"
    DOCUMENT = "Document"
    LANGUAGE = "Language"
    DOWNLOAD = "Download"
    QUESTION = "Question"
    SEND_FILL = "SendFill"
    COMPLETED = "Completed"
    CONSTRACT = "Constract"
    ALIGNMENT = "Alignment"
    BOOK_SHELF = "BookShelf"
    PENCIL_INK = "PencilInk"
    FOLDER_ADD = "FolderAdd"
    MICROPHONE = "Microphone"
    ARROW_DOWN = "ChevronDown"
    TRANSPARENT = "Transparent"
    MUSIC_FOLDER = "MusicFolder"
    CHEVRON_RIGHT = "ChevronRight"
    BACKGROUND_FILL = "BackgroundColor"
    FLUORESCENT_PEN = "FluorescentPen"

    def path(self, theme=Theme.AUTO):
        if theme == Theme.AUTO:
            c = getIconColor()
        else:
            c = "white" if theme == Theme.DARK else "black"

        return f':/qfluentwidgets/images/icons/{self.value}_{c}.svg'
