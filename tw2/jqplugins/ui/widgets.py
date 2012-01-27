
# tw2-proper imports
import tw2.core as twc
import tw2.forms as twf

# imports from this package
from tw2.jqplugins.ui import base as uibase

# generic imports
import types

class html(types.UnicodeType):
    """ A stand-in used to treat the item contents as 'html-literals' """
    def __html__(self):
        return unicode(self)

class AccordionWidget(uibase.JQueryUIWidget):
    """
    Click headers to expand/collapse content that is broken into
    logical sections, much like tabs. Optionally, toggle sections
    open/closed on mouseover.

    The underlying HTML markup is a series of headers (H3 tags) and
    content divs so the content is usable without JavaScript.
    
    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/accordion/

    List of options passable to the ``options`` parameter
        disabled -- boolean (default: False)
            Disables (true) or enables (false) the accordion. Can be set
            when initialising (first creating) the accordion.

        active -- selector, element, jQuery, boolean, number (default: first child)
            Selector for the active element. Set to false to display none at
            start. Needs ``collapsible: true``.

        animated -- boolean, str (default: 'slide')
            Choose your favorite animation, or disable them (set to false). In
            addition to the default, 'bounceslide' and all defined easing
            methods are supported ('bounceslide' requires UI Effects Core).

        autoHeight -- boolean (default: True)
            If set, the highest content part is used as height reference
            for all other parts. Provides more consistent animations.

        clearStyle -- boolean (default: False)
            If set, clears height and overflow styles after finishing
            animations. This enables accordions to work with dynamic content.
            Won't work together with autoHeight.

        collapsible -- boolean (default: False)
            Whether all the sections can be closed at once. Allows collapsing
            the active section by the triggering event (click is the default).

        event -- str (default: 'click')
            The event on which to trigger the accordion.

        fillSpace -- boolean (default: False)
            If set, the accordion completely fills the height of the parent
            element. Overrides autoheight.

        header -- selector, jQuery (default: '> li > :first-child,> :not(li):even')
            Selector for the header element.
        
        icons -- dict (default: {'header': 'ui-icon-triangle-1-e', 'headerSelected': 'ui-icon-triangle-1-s'})
            Icons to use for headers. Icons may be specified for 'header'
            and 'headerSelected', and we recommend using the icons native
            to the jQuery UI CSS Framework manipulated by jQuery UI
            ThemeRoller.

        navigation -- boolean (default: False)
            If set, looks for the anchor that matches location.href and
            activates it. Great for href-based state-saving. Use
            navigationFilter to implement your own matcher.

        navigationFilter -- javascript string (default: '')
            Overwrite the default location.href-matching with your own matcher.

    """

    template = "tw2.jqplugins.ui.templates.accordion"
    jqmethod = "accordion"

    items = twc.Param(
        'A list of (header (str), content (str)) tuples', default=[])

    def prepare(self):
        super(AccordionWidget, self).prepare()
        self.items = [(html(h), html(c)) for h, c in self.items]


class AutocompleteWidget(uibase.JQueryUIWidget, twf.TextField):
    """
    The Autocomplete widgets provides suggestions while you type into
    the field. Here the suggestions are tags for programming languages,
    give "ja" (for Java or JavaScript) a try.

    The datasource is a simple JavaScript array, provided to the widget
    using the source-option.

    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/autocomplete/

    List of options passable to the ``options`` parameter
        disabled -- boolean (default: False)
            Disables (true) or enables (false) the autocomplete. Can be set
            when initialising (first creating) the autocomplete.

        delay -- int (default: 300)
            The delay in milliseconds the Autocomplete waits after a
            keystroke to activate itself. A zero-delay makes sense for local
            data (more responsive), but can produce a lot of load for remote
            data, while being less responsive.

        minLength -- int (default: 1)
            The minimum number of characters a user has to type before the
            Autocomplete activates. Zero is useful for local data with just a
            few items. Should be increased when there are a lot of items,
            where a single character would match a few thousand items.

        source -- str, list, callback (default: None)
            Defines the data to use, must be specified. See
            http://jqueryui.com/demos/autocomplete/ for more details, and
            look at the various demos. 
    """
    template = "tw2.jqplugins.ui.templates.autocomplete"
    jqmethod = "autocomplete"

class CategoryAutocompleteWidget(AutocompleteWidget):
    """
    Implements the same API and functionality as the AutocompleteWidget
    with the exception that the data must be a list of dicts each with
    'label' and 'category' keys.

    """
    template = "tw2.jqplugins.ui.templates.catcomplete"
    jqmethod = "catcomplete"

    def prepare(self):
        # Adding the custom hook to jquery ui must be executed before
        #   all other js references to jquery ui are executed on the client.
        super(CategoryAutocompleteWidget, self).prepare()
        self.resources.append(uibase.jquery_ui_catcomplete_js)


class ButtonWidget(uibase.JQueryUIWidget):
    """
    A button with a javascript callback with different markup flavors.

    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/button/

    List of options passable to the ``options`` parameter
        disabled -- boolean (default: False)
            Disables (true) or enables (false) the button. Can be set
            when initialising (first creating) the button.

        text -- boolean (default: True)
            Whether to show any text - when set to false (display no text),
            icons (see icons option) must be enabled, otherwise it'll be
            ignored.

        icons -- dict (default: {'primary' : None, 'secondary' : None})
            Icons to display, with or without text (see text option). The
            primary icon is displayed by default on the left of the label
            text, the secondary by default is on the right. Value for the
            primary and secondary properties must be a classname (String),
            eg. "ui-icon-gear".
            For using only one icon: ``icons: {primary:'ui-icon-locked'}``.
            For using two icons:
            ``icons: {primary:'ui-icon-gear',secondary:'ui-icon-triangle-1-s'}``

        label -- str (default: "HTML content of the button")
            Text to show on the button. When not specified (null), the
            element's html content is used, or its value attribute when
            it's an input element of type submit or reset; or the html
            content of the associated label element if its an input of type
            radio or checkbox

    """
    template = "tw2.jqplugins.ui.templates.button"
    jqmethod = "button"

    type = twc.Param(
        'Type of button.  Valid values are "button", "input", "anchor"',
        default='button')

class ButtonSetRadio(uibase.JQueryUIWidget):
    """
    Styles a group of radio buttons as a 'button set' by calling
    ``.buttonset()`` on a common container.
    
    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/button/#radio
    """
    template = 'tw2.jqplugins.ui.templates.buttonset_radio'
    
    items = twc.Param("a list of dicts - required keys are 'id' and 'label'",
                      default=[])
    checked_item = twc.Param("a single button may be marked as 'checked' by " +
                             "passing its 'id' [as a string] to this parameter",
                             default=None)
    jqmethod = "buttonset"

    def prepare(self):
        super(ButtonSetRadio, self).prepare()

        if not isinstance(self.items, list):
            raise ValueError, "'items' must be of type list"
            
        ids = [i['id'] for i in self.items]
        if self.checked_item and self.checked_item not in ids:
                raise ValueError, "A 'checked_item' has been passed in but " + \
                                  "the id to which it refers is not in the " + \
                                  "'items' list"
            

class ButtonSetCheckbox(uibase.JQueryUIWidget):
    """
    Styles a group of checkboxes as a 'button set' by calling ``.buttonset()``
    on a common container.
    
    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/button/#checkbox
    """
    template = 'tw2.jqplugins.ui.templates.buttonset_checkbox'
    
    items = twc.Param("a list of dicts - required keys are 'id', 'label' " +
                      "and (optionally) 'isSelected' [boolean]", default=[])
    jqmethod = "buttonset"

    def prepare(self):
        super(ButtonSetCheckbox, self).prepare()

        if not isinstance(self.items, list):
            raise ValueError, "'items' must be of type list"
            
        # plug in value 'isSelected'=False if 'isSelected' not present in dict
        for i in self.items:
            if not i.has_key('isSelected'):
                i['isSelected'] = False


class DatePickerWidget(uibase.JQueryUIWidget, twf.TextField):
    """
    The datepicker is tied to a standard form input field.
    Focus on the input (click, or use the tab key) to open an
    interactive calendar in a small overlay.  Choose a date, click
    elsewhere on the page (blur the input), or hit the Esc key to
    close.  If a date is chosen, feedback is shown as the input's
    value.
    
    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/datepicker/

    List of options passable to the ``options`` parameter
        disabled -- boolean (default: False)
            Disables (true) or enables (false) the datepicker. Can be set
            when initialising (first creating) the datepicker.
        
        altField -- str (default: '')
            The jQuery selector for another field that is to be updated
            with the selected date from the datepicker. Use the altFormat
            setting to change the format of the date within this field.
            Leave as blank for no alternate field.
        
        altFormat -- str (default: '')
            The dateFormat to be used for the altField option. This
            allows one date format to be shown to the user for selection
            purposes, while a different format is actually sent behind the
            scenes. For a full list of the possible formats see the
            jQuery formatDate function
        
        appendText -- str (default: '')
            The text to display after each date field, e.g. to show the
            required format.
        
        autoSize -- boolean (default: False)
            Set to true to automatically resize the input field to
            accomodate dates in the current dateFormat.
        
        buttonImage -- str (default: '')
            The URL for the popup button image. If set, buttonText becomes
            the alt value and is not directly displayed.
        
        buttonImageOnly -- boolean (default: False)
            Set to true to place an image after the field to use as the
            trigger without it appearing on a button.
        
        buttonText -- str (default: '...')
            The text to display on the trigger button. Use in conjunction
            with showOn equal to 'button' or 'both'.
        
        calculateWeek -- JSSymbol (default : $.datepicker.iso8601Week)
            A function to calculate the week of the year for a given date.
            The default implementation uses the ISO 8601 definition: weeks
            start on a Monday; the first week of the year contains the first
            Thursday of the year.
        
        changeMonth -- boolean (default: False)
            Allows you to change the month by selecting from a drop-down
            list. You can enable this feature by setting the attribute to true.
        
        changeYear -- boolean (default: False)
            Allows you to change the year by selecting from a drop-down
            list. You can enable this feature by setting the attribute to
            true. Use the yearRange option to control which years are made
            available for selection.
        
        closeText -- str (default: 'Done')
            The text to display for the close link. This attribute is one
            of the regionalisation attributes. Use the showButtonPanel to
            display this button.
        
        constrainInput -- boolean (default: True)
            When true entry in the input field is constrained to those
            characters allowed by the current dateFormat.
        
        currentText -- str (default: 'Today')
            The text to display for the current day link. This attribute
            is one of the regionalisation attributes. Use the
            showButtonPanel to display this button.
        
        dateFormat -- str (default: 'mm/dd/yy')
            The format for parsed and displayed dates. This attribute is
            one of the regionalisation attributes. For a full list of the
            possible formats see the formatDate function.
        
        dayNames -- list (default:['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
            The list of long day names, starting from Sunday, for use as
            requested via the dateFormat setting. They also appear as popup
            hints when hovering over the corresponding column headings. This
            attribute is one of the regionalisation attributes.
        
        dayNamesMin -- list (default:['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'])
            The list of minimised day names, starting from Sunday, for use
            as column headers within the datepicker. This attribute is one
            of the regionalisation attributes.
        
        dayNamesShort -- list (default:['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
            The list of abbreviated day names, starting from Sunday, for
            use as requested via the dateFormat setting. This attribute
            is one of the regionalisation attributes.
        
        defaultDate -- date, number, str (default: None)
            Set the date to highlight on first opening if the field is
            blank. Specify either an actual date via a Date object or as a
            string in the current dateFormat, or a number of days from
            today (e.g. +7) or a string of values and periods ('y' for
            years, 'm' for months, 'w' for weeks, 'd' for days,
            e.g. '+1m +7d'), or null for today.
        
        duration -- str, number (default: 'normal')
            Control the speed at which the datepicker appears, it may be
            a time in milliseconds or a string representing one of the three
            predefined speeds ("slow", "normal", "fast").
        
        firstDay -- number (default: 0)
            Set the first day of the week: Sunday is 0, Monday is 1, ...
            This attribute is one of the regionalisation attributes.
        
        gotoCurrent -- boolean (default: False)
            When true the current day link moves to the currently selected
            date instead of today.
        
        hideIfNoPrevNext -- boolean (default: False)
            Normally the previous and next links are disabled when not
            applicable (see minDate/maxDate). You can hide them altogether
            by setting this attribute to true.
        
        isRTL -- boolean (default: False)
            True if the current language is drawn from right to left. This
            attribute is one of the regionalisation attributes.
        
        maxDate -- date, number, str (default: None)
            Set a maximum selectable date via a Date object or as a string
            in the current dateFormat, or a number of days from
            today (e.g. +7) or a string of values and periods ('y' for
            years, 'm' for months, 'w' for weeks, 'd' for days,
            e.g. '+1m +1w'), or None for no limit.
        
        minDate -- date, number, str (default: None)
            Set a minimum selectable date via a Date object or as a string
            in the current dateFormat, or a number of days from today (e.g. +7)
            or a string of values and periods ('y' for years, 'm' for months,
            'w' for weeks, 'd' for days, e.g. '-1y -1m'), or None for no limit.

        monthNames -- list (default: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
            The list of full month names, for use as requested via the
            dateFormat setting. This attribute is one of the
            regionalisation attributes.
        
        monthNamesShort -- list (default: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
            The list of abbreviated month names, as used in the month
            header on each datepicker and as requested via the dateFormat
            setting. This attribute is one of the regionalisation attributes.
        
        navigationAsDateFormat -- bool (default: False)
            When true the formatDate function is applied to the prevText,
            nextText, and currentText values before display, allowing them
            to display the target month names for example.
        
        nextText -- str (default: 'Next')
            The text to display for the next month link. This attribute
            is one of the regionalisation attributes. With the standard
            ThemeRoller styling, this value is replaced by an icon.
        
        numberOfMonths -- number, list (default: 1)
            Set how many months to show at once. The value can be a
            straight integer, or can be a two-element array to define the
            number of rows and columns to display.
        
        prevText -- str (default: 'Prev')
            The text to display for the previous month link. This attribute
            is one of the regionalisation attributes. With the standard
            ThemeRoller styling, this value is replaced by an icon.
        
        selectOtherMonths -- boolean (default: False)
            When true days in other months shown before or after the
            current month are selectable. This only applies if
            showOtherMonths is also true.
        
        shortYearCutoff -- str, number (default: '+10')
            Set the cutoff year for determining the century for a date
            (used in conjunction with dateFormat 'y'). If a numeric
            value (0-99) is provided then this value is used directly. If
            a string value is provided then it is converted to a number and
            added to the current year. Once the cutoff year is calculated,
            any dates entered with a year value less than or equal to it are
            considered to be in the current century, while those greater than
            it are deemed to be in the previous century.
        
        showAnim -- str (default: 'show')
            Set the name of the animation used to show/hide the
            datepicker. Use 'show' (the default), 'slideDown', 'fadeIn',
            any of the show/hide jQuery UI effects, or '' for no animation.
        
        showButtonPanel -- boolean (default: False)
            Whether to show the button panel.
        
        showCurrentAtPos -- number (default: 0)
            Specify where in a multi-month display the current month
            shows, starting from 0 at the top/left.
        
        showMonthAfterYear -- boolean (default: False)
            Whether to show the month after the year in the header. This
            attribute is one of the regionalisation attributes.
        
        showOn -- str (default: 'focus')
            Have the datepicker appear automatically when the field
            receives focus ('focus'), appear only when a button is
            clicked ('button'), or appear when either event takes
            place ('both').
        
        showOptions -- dict (default: {})
            If using one of the jQuery UI effects for showAnim, you can
            provide additional settings for that animation via this option.
        
        showOtherMonths -- boolean (default: False)
            Display dates in other months (non-selectable) at the start
            or end of the current month. To make these days selectable
            use selectOtherMonths.
        
        showWeek -- boolean (default: False)
            When true a column is added to show the week of the year.
            The calculateWeek option determines how the week of the year
            is calculated. You may also want to change the firstDay option.
        
        stepMonths -- number (default: 1)
            Set how many months to move when clicking the Previous/Next links.
        
        weekHeader -- str (default: 'Wk')
            The text to display for the week of the year column heading.
            This attribute is one of the regionalisation attributes. Use
            showWeek to display this column.
        
        yearRange -- str (default: 'c-10:c+10')
            Control the range of years displayed in the year drop-down:
            either relative to today's year (-nn:+nn), relative to the
            currently selected year (c-nn:c+nn), absolute (nnnn:nnnn), or
            combinations of these formats (nnnn:-nn). Note that this option
            only affects what appears in the drop-down, to restrict which
            dates may be selected use the minDate and/or maxDate options.
        
        yearSuffix -- str (default: '')
            Additional text to display after the year in the month headers.
            This attribute is one of the regionalisation attributes.


        beforeShow -- JSSymbol (default: None) -- function(input, inst)
            Can be a function that takes an input field and current
            datepicker instance and returns an options object to update
            the datepicker with. It is called just before the datepicker
            is displayed.

        beforeShowDay -- JSSymbol (default: None) -- function(date)
            The function takes a date as a parameter and must return an
            array with [0] equal to true/false indicating whether or not
            this date is selectable, [1] equal to a CSS class name(s) or ''
            for the default presentation, and [2] an optional popup tooltip
            for this date. It is called for each day in the datepicker before
            it is displayed.

        onChangeMonthYear -- JSSymbol (default: None) -- function(year, month, inst)
            Allows you to define your own event when the datepicker moves
            to a new month and/or year. The function receives the selected
            year, month (1-12), and the datepicker instance as parameters.
            ``this`` refers to the associated input field.

        onClose -- JSSymbol (default: None) -- function(dateText, inst)
            Allows you to define your own event when the datepicker is
            closed, whether or not a date is selected. The function receives
            the selected date as text ('' if none) and the datepicker
            instance as parameters. this refers to the associated input field.

        onSelect -- JSSymbol (default: None) -- function(dateText, inst)
            Allows you to define your own event when the datepicker is
            selected. The function receives the selected date as text
            and the datepicker instance as parameters. this refers to the
            associated input field.
    """
    template = "tw2.jqplugins.ui.templates.datepicker"
    jqmethod = "datepicker"

class DialogWidget(uibase.JQueryUIWidget):
    """
    The basic dialog window is an overlay positioned within the
    viewport and is protected from page content (like select elements)
    shining through with an iframe. It has a title bar and a content
    area, and can be moved, resized and closed with the 'x' icon by default.
    
    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/dialog/

    List of options passable to the ``options`` parameter
        disabled -- boolean (default: False)
            Disables (true) or enables (false) the dialog. Can be set when
            initialising (first creating) the dialog.

        autoOpen -- boolean (default:  True)
            When autoOpen is true the dialog will open automatically when
            dialog is called. If false it will stay hidden
            until .dialog("open") is called on it.

        buttons -- dict (default: {})
            Specifies which buttons should be displayed on the dialog. The
            property key is the text of the button. The value is the callback
            function for when the button is clicked. The context of the
            callback is the dialog element; if you need access to the
            button, it is available as the target of the event object.

        closeOnEscape -- boolean (default:  True)
            Specifies whether the dialog should close when it has focus
            and the user presses the esacpe (ESC) key.

        closeText -- str (default: 'close')
            Specifies the text for the close button. Note that the close
            text is visibly hidden when using a standard theme.

        dialogClass -- str (default: '')
            The specified class name(s) will be added to the dialog, for
            additional theming.

        draggable -- boolean (default:  True)
            If set to true, the dialog will be draggable will be
            draggable by the titlebar.

        height -- number (default: 'auto')
            The height of the dialog, in pixels. Specifying 'auto' is also
            supported to make the dialog adjust based on its content.

        hide -- str (default:  None)
            The effect to be used when the dialog is closed.

        maxHeight -- number (default: False)
            The maximum height to which the dialog can be resized, in pixels.

        maxWidth -- number (default: False)
            The maximum width to which the dialog can be resized, in pixels.

        minHeight -- number (default: 150)
            The minimum height to which the dialog can be resized, in pixels.

        minWidth -- number (default: 150)
            The minimum width to which the dialog can be resized, in pixels.

        modal -- boolean (default: False)
            If set to true, the dialog will have modal behavior; other
            items on the page will be disabled (i.e. cannot be interacted
            with). Modal dialogs create an overlay below the dialog but above
            other page elements.
    
        position -- str, list (default: 'center')
            Specifies where the dialog should be displayed. Possible values: 
                1) a single string representing position within
                viewport: 'center', 'left', 'right', 'top', 'bottom'. 

                2) an array containing an x,y coordinate pair in pixel
                offset from left, top corner of viewport (e.g. [350,100]) 

                3) an array containing x,y position string values 
                (e.g. ['right','top'] for top right corner).

        resizable -- boolean (default:  True)
            If set to true, the dialog will be resizeable.

        show -- str (default:  None)
            The effect to be used when the dialog is opened.

        stack -- boolean (default:  True)
            Specifies whether the dialog will stack on top of other dialogs.
            This will cause the dialog to move to the front of other dialogs
            when it gains focus.

        title -- str (default: '')
            Specifies the title of the dialog. The title can also be
            specified by the title attribute on the dialog source element.

        width -- number (default: 300)
            The width of the dialog, in pixels.

        zIndex -- int (default: 1000)
            The starting z-index for the dialog.

        onSelect -- JSSymbol (default: None) -- function(dateText, inst)

        beforeclose -- JSSymbolc (default: None) -- function(event, ui)
            This event is triggered when a dialog attempts to close. If
            the beforeclose event handler (callback function) returns false,
            the close will be prevented.

        open -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when dialog is opened.

        focus -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when the dialog gains focus.

        dragStart -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered at the beginning of the dialog being
            dragged.

        drag -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when the dialog is dragged.

        dragStop -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered after the dialog has been dragged.

        resizeStart -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered at the beginning of the dialog being
            resized.

        resize -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when the dialog is resized.

        resizeStop -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered after the dialog has been resized.

        close -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when the dialog is closed.
    """
    template = "tw2.jqplugins.ui.templates.dialog"
    jqmethod = "dialog"
    
    value = twc.Param('The HTML message for the dialog')
    
    def prepare(self):
        super(DialogWidget, self).prepare()
        # The following is done to treat the items contents as 'html-literals'
        self.value = html(self.value)

class ProgressBarWidget(uibase.JQueryUIWidget):
    """
    The progress bar is designed to simply display the current % complete
    for a process. The bar is coded to be flexibly sized through CSS and
    will scale to fit inside it's parent container by default.
    
    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/progressbar/

    List of options passable to the ``options`` parameter
        disabled -- boolean (default: False)
            Disables (true) or enables (false) the progressbar. Can
            be set when initialising (first creating) the progressbar.

        value -- number (default: 0)
            The value of the progressbar.

        change -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when the value of the progressbar changes.
    """
    template = "tw2.jqplugins.ui.templates.progressbar"
    jqmethod = "progressbar"

class SliderWidget(uibase.JQueryUIWidget):
    """
    The jQuery UI Slider plugin makes selected elements into sliders.
    There are various options such as multiple handles, and ranges. The
    handle can be moved with the mouse or the arrow keys.
    
    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/slider/

    List of options passable to the ``options`` parameter
        disabled -- boolean (default: False)
            Disables (true) or enables (false) the slider. Can be set when
            initialising (first creating) the slider.
        
        animate -- boolean, str, number (default: False)
            Whether to slide handle smoothly when user click outside handle
            on the bar. Will also accept a string representing one of the
            three predefined speeds ("slow", "normal", or "fast") or the
            number of milliseconds to run the animation (e.g. 1000).

        max -- number (default: 100)
            The maximum value of the slider.

        min -- number (default: 0)
            The minimum value of the slider.

        orientation -- str (default: 'horizontal')
            This option determines whether the slider has the min at the
            left, the max at the right or the min at the bottom, the max
            at the top. Possible values: 'horizontal', 'vertical'.

        range -- boolean, str, (default: False)
            If set to true, the slider will detect if you have two handles
            and create a stylable range element between these two. Two other
            possible values are 'min' and 'max'. A min range goes from the
            slider min to one handle. A max range goes from one handle to
            the slider max.

        step -- number (default: 1)
            Determines the size or amount of each interval or step the
            slider takes between min and max. The full specified value
            range of the slider (max - min) needs to be evenly divisible
            by the step.

        value -- number (default: 0)
            Determines the value of the slider, if there's only one handle.
            If there is more than one handle, determines the value of the
            first handle.

        values -- list (default: None)
            This option can be used to specify multiple handles. If range
            is set to true, the length of 'values' should be 2.

        start -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when the user starts sliding.

        slide -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered on every mouse move during slide.
            Use ui.value (single-handled sliders) to obtain the value
            of the current handle, $(..).slider('value', index) to get
            another handles' value.

            Return false in order to prevent a slide, based on ui.value.

        change -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered on slide stop, or if the value is
            changed programmatically (by the value method). Takes arguments
            event and ui. Use event.orginalEvent to detect whether the value
            changed by mouse, keyboard, or programmatically. Use ui.value
            (single-handled sliders) to obtain the value of the current
            handle, $(this).slider('values', index) to get another
            handle's value.

        stop -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when the user stops sliding.
    """
    template = "tw2.jqplugins.ui.templates.slider"
    jqmethod = "slider"

class TabsWidget(uibase.JQueryUIWidget):
    """
    Tabs are generally used to break content into multiple sections that
    can be swapped to save space, much like an accordion.

    By default a tab widget will swap between tabbed sections onClick, but
    the events can be changed to onHover through an option. Tab content can
    be loaded via Ajax by setting an href on a tab.
    
    See the wrapped library's documentation for more information:
        http://jqueryui.com/demos/tabs/

    List of options passable to the ``options`` parameter
        disabled -- boolean (default: False)
            Disables (true) or enables (false) the tabs. Can be set when
            initialising (first creating) the tabs.

        ajaxOptions -- dict (default: {})
            Additional Ajax options to consider when loading tab
            content (see $.ajax).

        cache -- boolean (default: False)
            Whether or not to cache remote tabs content, e.g. load only
            once or with every click. Cached content is being lazy loaded,
            e.g once and only once for the first click. Note that to
            prevent the actual Ajax requests from being cached by the
            browser you need to provide an extra cache: false flag to
            ajaxOptions.

        collapsible -- boolean (default: False)
            Set to true to allow an already selected tab to become
            unselected again upon reselection.

        cookie -- dict (default: None)
            Store the latest selected tab in a cookie. The cookie is then
            used to determine the initially selected tab if the selected
            option is not defined. Requires cookie plugin. The object
            needs to have key/value pairs of the form the cookie plugin
            expects as options. Available options (example): { expires: 7,
            path: '/', domain: 'jquery.com', secure: true }. Since jQuery
            UI 1.7 it is also possible to define the cookie name being used
            via name property.

        deselectable -- boolean (default: False)
            deprecated in jQuery UI 1.7, use collapsible.

        disabled -- list (default: [])
            An array containing the position of the tabs (zero-based index)
            that should be disabled on initialization.

        event -- str (default: 'click')
            The type of event to be used for selecting a tab.

        fx -- dict, list (default: None)
            Enable animations for hiding and showing tab panels. The
            duration option can be a string representing one of the three
            predefined speeds ("slow", "normal", "fast") or the duration
            in milliseconds to run an animation (default is "normal").

        idPrefix -- str (default: 'ui-tabs-')
            If the remote tab, its anchor element that is, has no title
            attribute to generate an id from, an id/fragment identifier is
            created from this prefix and a unique id returned
            by $.data(el), for example "ui-tabs-54".

        panelTemplate -- str (default: '<div></div>')
            HTML template from which a new tab panel is created in case
            of adding a tab with the add method or when creating a panel
            for a remote tab on the fly.

        selected -- number (default: 0)
            Zero-based index of the tab to be selected on initialization.
            To set all tabs to unselected pass -1 as value.

        spinner -- str (default: '<em>Loading&#8230;</em>')
            The HTML content of this string is shown in a tab title while
            remote content is loading. Pass in empty string to deactivate
            that behavior. An span element must be present in the A tag
            of the title, for the spinner content to be visible.

        tabTemplate -- str (default: '<li><a href="#{href}"><span>#{label}</span></a></li>')
            HTML template from which a new tab is created and added. The
            placeholders #{href} and #{label} are replaced with the url
            and tab label that are passed as arguments to the add method.

        select -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when clicking a tab.

        load -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered after the content of a remote tab has
            been loaded.

        show -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when a tab is shown.

        add -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when a tab is added.

        remove -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when a tab is removed.

        enable -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when a tab is enabled.

        disable -- JSSymbol (default: None) -- function(event, ui)
            This event is triggered when a tab is disabled.
    """
    template = "tw2.jqplugins.ui.templates.tabs"
    jqmethod = "tabs"
    
    items = twc.Param(
        'A list of dicts, possible keys are "href", "label", and "content"',
        default=[])
    
    def prepare(self):
        super(TabsWidget, self).prepare()

        if not isinstance(self.items, list):
            raise ValueError, 'items must be of type list'

        if len(self.items) == 0:
            # Whatevah.
            return

        # Otherwise, if its an old-style list of tuples, convert it to the
        #  new style.
        if isinstance(self.items[0], tuple):
            import warnings
            warnings.warn('list-of-tuples format for items is deprecated',
                          DeprecationWarning)
            self.items = [{'label': v[0], 'content': v[1]} for v in self.items]

        for i in range(len(self.items)):
            for k in self.items[i].keys():
                self.items[i][k] = html(self.items[i][k])

