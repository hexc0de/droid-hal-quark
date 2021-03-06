# These and other macros are documented in dhd/droid-hal-device.inc
%define device quark
%define vendor motorola
%define vendor_pretty Motorola
%define device_pretty Droid Turbo

%define installable_zip 1

%define droid_target_armv7hl 1

%define straggler_files \
/init.mmi.boot.sh \
/init.mmi.touch.sh \
/init.mmi.usb.sh \
%{nil}

%define android_config \
#define QCOM_BSP 1\
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}


%include rpm/dhd/droid-hal-device.inc
