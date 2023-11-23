from winreg import HKEY_CURRENT_USER


class Path:
    class Translations:
        Hindi: str = "Translations/hi-in.json"

    class IconPaths:
        AppliedIcon = "Assets/icons/applied.png"

        class Light:
            ResetIcon: str = "Assets/icons/light/reset_icon.png"
            ColorPicker: str = "Assets/icons/light/color_picker_icon.png"
            Logo: str = "Assets/icons/light/logo.png"
            MinimizeIcon: str = "Assets/icons/light/minimize_icon.png"
            UpArrow: str = "Assets/icons/light/up-arrow.png"
            DownArrow: str = "Assets/icons/light/down-arrow.png"
            CloseIcon: str = "Assets/icons/light/close_icon.png"
            BackIcon: str = "Assets/icons/light/back_icon.png"
            DownloadIcon: str = "Assets/icons/light/download_icon.png"
            ExternalIcon: str = "Assets/icons/light/external_icon.png"
            InternalIcon: str = "Assets/icons/light/internal_icon.png"
            FolderIcon: str = "Assets/icons/light/folder_icon.png"
            InstallIcon: str = "Assets/icons/light/install_icon.png"
            UninstallIcon: str = "Assets/icons/light/uninstall_icon.png"
            Logo: str = "Assets/icons/light/logo.png"
            RunIcon: str = "Assets/icons/light/run_icon.png"
            StopIcon: str = "Assets/icons/light/stop_icon.png"
            SettingsIcon: str = "Assets/icons/light/settings_icon.png"

        class Dark:
            ResetIcon: str = "Assets/icons/dark/reset_icon.png"
            ColorPicker: str = "Assets/icons/dark/color_picker_icon.png"
            Logo: str = "Assets/icons/dark/logo.png"
            MinimizeIcon: str = "Assets/icons/dark/minimize_icon.png"
            UpArrow: str = "Assets/icons/dark/up-arrow.png"
            DownArrow: str = "Assets/icons/dark/down-arrow.png"
            CloseIcon: str = "Assets/icons/dark/close_icon.png"
            BackIcon: str = "Assets/icons/dark/back_icon.png"
            DownloadIcon: str = "Assets/icons/dark/download_icon.png"
            ExternalIcon: str = "Assets/icons/dark/external_icon.png"
            InternalIcon: str = "Assets/icons/dark/internal_icon.png"
            FolderIcon: str = "Assets/icons/dark/folder_icon.png"
            InstallIcon: str = "Assets/icons/dark/install_icon.png"
            UninstallIcon: str = "Assets/icons/dark/uninstall_icon.png"
            Logo: str = "Assets/icons/dark/logo.png"
            RunIcon: str = "Assets/icons/dark/run_icon.png"
            StopIcon: str = "Assets/icons/dark/stop_icon.png"
            SettingsIcon: str = "Assets/icons/dark/settings_icon.png"

    class FontPaths:
        NunitoSans: str = "Assets/fonts/NunitoSans_10pt_Condensed-Regular.ttf"
        AndikaRegular: str = "Assets/fonts/Andika-Regular.ttf"

    class RegPaths:
        BasePath: str = r"Software\\TranslucentFlyouts\\"
        Software: str = r"Software\\"
        TranslucentFlyouts: str = r"TranslucentFlyouts\\"
        Global: str = ""
        DropDown: str = r"DropDown\\"
        Menu: str = r"Menu\\"
        Animation: str = r"Animation\\"
        Hot: str = r"Hot\\"
        DisabledHot: str = r"DisabledHot\\"
        Focusing: str = r"Focusing\\"
        Separator: str = r"Separator\\"
        Tooltip: str = r"Tooltip\\"

    class RegKeys:
        BaseKey: int = HKEY_CURRENT_USER
        TranslucentFlyouts: str = "TranslucentFlyouts"
        DropDown: str = "DropDown"
        Menu: str = "Menu"
        Animation: str = "Animation"
        Hot: str = "Hot"
        DisabledHot: str = "DisabledHot"
        Focusing: str = "Focusing"
        Separator: str = "Separator"
        Tooltip: str = "Tooltip"
        EffectType: str = "EffectType"
        EnableDropShadow: str = "EnableDropShadow"
        DarkModeBorderColor: str = "DarkMode_BorderColor"
        LightModeBorderColor: str = "LightMode_BorderColor"
        DarkModeGradientColor: str = "DarkMode_GradientColor"
        LightModeGradientColor: str = "LightMode_GradientColor"
        DarkModeColor: str = "DarkMode_Color"
        LightModeColor: str = "LightMode_Color"
        Disabled: str = "Disabled"
        NoSystemDropShadow: str = "NoSystemDropShadow"
        EnableImmersiveStyle: str = "EnableImmersiveStyle"
        EnableCustomRendering: str = "EnableCustomRendering"
        EnableFluentAnimation: str = "EnableFluentAnimation"
        NoModernAppBackgroundColor: str = "NoModernAppBackgroundColor"
        ColorTreatAsTransparent: str = "ColorTreatAsTransparent"
        ColorTreatAsTransparentThreshold: str = "ColorTreatAsTransparentThreshold"
        FadeOutTime: str = "FadeOutTime"
        PopInTime: str = "PopInTime"
        FadeInTime: str = "FadeInTime"
        PopInStyle: str = "PopInStyle"
        StartRatio: str = "StartRatio"
        EnableImmediateInterupting: str = "EnableImmediateInterupting"
        CornerRadius: str = "CornerRadius"
        EnableThemeColorization: str = "EnableThemeColorization"
        NoBorderColor: str = "NoBorderColor"
        CornerType: str = "CornerType"
        Width: str = "Width"
