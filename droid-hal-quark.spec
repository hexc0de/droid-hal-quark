# These and other macros are documented in dhd/droid-hal-device.inc
%define device quark
%define vendor motorola
%define vendor_pretty Motorola
%define device_pretty "Droid Turbo"
%define installable_zip 1
%define straggler_files \
/init.mmi.boot.sh \
/init.mmi.touch.sh \
/init.mmi.usb.sh \
%{nil}
%define android_config \
#define QCOM_BSP 1 \
%{nil}
%include rpm/dhd/droid-hal-device.inc
