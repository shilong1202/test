_base_ = [
    'F:/Seg/mmsegMedical/configs/_base_/models/unet.py', '../_base_/datasets/isic2017.py',
    '../_base_/default_runtime.py'
]
crop_size = (256, 256)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    decode_head=dict(
            loss_decode=[
                dict(type='mmseg.CrossEntropyLoss', loss_name='loss_ce', use_sigmoid=False, loss_weight=1.0),
            ]
    )

)

optimizer=dict(type='AdamW', lr=0.005, betas=(0.9, 0.999), weight_decay=0.05)
optim_wrapper = dict(type='OptimWrapper', optimizer=optimizer)

train_cfg = dict(type='IterBasedTrainLoop', max_iters=20000, val_interval=2000)
param_scheduler = [
    dict(
        type='LinearLR', start_factor=1e-6, by_epoch=False, begin=0, end=1000),
    dict(
        type='PolyLR',
        power=1.0,
        begin=1000,
        end=20000,
        eta_min=0.0,
        by_epoch=False,
    )
]